from profanity_check import predict, predict_prob
from clean_transcription import parse_audio_ouput

def get_prof_result(x):
    x["is_profanity"] = predict([x["text"]])[0] == 1
    x["profane_prob"] = predict_prob([x["text"]])[0]
    return x

def detect_profanity(lines):
    lines_with_prof = list(map(lambda x: get_prof_result(x), lines))
    return lines_with_prof

if __name__ == "__main__":
    path = "/mnt/c/Users/danie/Workspace/whisper-clean-media/media_cleaner/output.txt"
    with open(path, "r", encoding="ISO-8859-1") as f:
        result = parse_audio_ouput(f.read())
        lines_with_prof = detect_profanity(result)
        for line in lines_with_prof:
            if line["is_profanity"] and line["profane_prob"] >= 0.9:
                print(line["text"] + " (" + str(line["profane_prob"]) + ")")
        