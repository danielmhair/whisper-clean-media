from profanity_check import predict, predict_prob
from clean_transcription import parse_audio_ouput
import re
import json
import os

def keep_letters(string):
    return re.sub("[^a-zA-Z]+", "", string)


def get_profanity_words():
    profanity_words = []
    try:
        if len(profanity_words) == 0:
            profanity_path = os.path.join(os.path.dirname(__file__), "profanity.json")
            with open(profanity_path, "r") as f:
                profanity_words = json.load(f)
                profanity_words = list(map(lambda x: x.lower(), profanity_words))
    except FileNotFoundError:
        profanity_words = []
    
    return profanity_words

def get_prof_result(x, profanity_words):
    cleaned_text = keep_letters(x["text"]).lower()
    x["is_profanity"] = len(list(filter(lambda x: x == cleaned_text, profanity_words))) > 0
    return x

def detect_profanity(lines):
    profanity_words = get_profanity_words()
    lines_with_prof = list(map(lambda x: get_prof_result(x, profanity_words), lines))
    return lines_with_prof


def main(path):
    with open(path, "r", encoding="ISO-8859-1") as f:
        result = parse_audio_ouput(f.read())
        lines_with_prof = detect_profanity(result)
        segments_to_mute = []
        for i, line in enumerate(lines_with_prof):
            if line["is_profanity"]:
                context = list(map(lambda x: x['text'], lines_with_prof[i-5:i+5]))
                print(" ".join(context) + " (" + line['text'] + ")")
                segments_to_mute.append((line["start_time"], line["end_time"]))
        # print(segments_to_mute)

if __name__ == "__main__":
    path = "/mnt/c/Users/danie/Workspace/whisper-clean-media/media_cleaner/output.txt"
    main(path)
