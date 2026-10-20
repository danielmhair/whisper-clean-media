# [00:00:00.000 --> 00:00:00.000]  
# [00:00:00.000 --> 00:00:00.210]   [
# [00:00:00.210 --> 00:00:00.420]  M
# [00:00:00.420 --> 00:00:01.020]  US
# [00:00:01.020 --> 00:00:01.260]  IC
# [00:00:01.260 --> 00:00:02.110]   PLAY
# [00:00:02.110 --> 00:00:02.740]  ING
# [00:00:02.740 --> 00:00:02.980]  ]
# [00:00:02.980 --> 00:00:02.980]  
# [00:00:02.980 --> 00:00:03.190]   [

# Parse text like above to get the following:
# 1. Start time
# 2. End time
# 3. Text

# Output:
# 1. A list of dictionaries with the above information, but with words completed

from lib2to3.pytree import convert
import os


def parse_audio_ouput(line_str):
    lines = list(filter(lambda x: x, line_str.split("\n")))
    text_dicts = []
    for line in lines:
        # parse out the start and end times
        start_time, end_and_rest = line[1:].split(" --> ")
        end_time_index = end_and_rest.index("]")
        end_time = end_and_rest[:end_time_index]
        text = end_and_rest[end_time_index+3:]
        print(start_time)
        print(end_time)
        print(text)
    
        text_dicts.append({
            "start_time": start_time,
            "end_time": end_time,
            "text": text
        })
    return convert_to_words(text_dicts)

def convert_to_words(text_dicts):
    clean_lines = []
    stack = []  # To hold lines that start with "[" or "("
    
    for line in text_dicts:
        # Check if a line starts with "[" or "("
        if line["text"].strip().startswith("[") or line["text"].strip().startswith("("):
            stack.append(line)
        # Check if a line ends with "]" or ")"
        elif line["text"].strip().endswith("]") or line["text"].strip().endswith(")"):
            if len(stack) > 0:
                # Merge from stack
                start_line = stack.pop(0)  # Pop the first element
                new_line = {
                    "start_time": start_line["start_time"],
                    "end_time": line["end_time"],
                    "text": start_line["text"]
                }
                
                # Concatenate all the lines in between and including the last line
                for interim_line in stack:
                    new_line["text"] += interim_line["text"]
                new_line["text"] += line["text"]
                
                # Clear the stack for the next set of brackets
                stack.clear()
                
                clean_lines.append(new_line)
        # Normal case (no special brackets)
        else:
            if line["text"] == "":
                continue
            if len(stack) > 0:
                stack.append(line)
                continue
            if len(clean_lines) == 0:
                clean_lines.append(line)
                continue
            
            if line["text"].startswith(" "):
                clean_lines.append(line)
            else:
                prev_line = clean_lines.pop()
                new_line = {
                    "start_time": prev_line["start_time"],
                    "end_time": line["end_time"],
                    "text": prev_line["text"] + line["text"]
                }
                clean_lines.append(new_line)
    return clean_lines

if __name__ == "__main__":
    path = "/mnt/c/Users/danie/Workspace/whisper-clean-media/media_cleaner/output.txt"
    with open(path, "r", encoding="ISO-8859-1") as f:
        result = parse_audio_ouput(f.read())
        print('')
        print(result)
