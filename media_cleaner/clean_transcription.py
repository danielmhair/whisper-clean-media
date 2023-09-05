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

def parse_text(line_str):
    lines = line_str.split("\n")
    for line in lines:
        # parse out the start and end times
        start_time, end_and_rest = line[1:].split(" --> ")
        end_time, rest = end_and_rest.split("]")
        print(start_time)
        print(end_time)
        text = rest[2:]
        print(text)

        


# Create test cases
test_case_1 = """[00:00:00.000 --> 00:00:00.000]  
[00:00:00.000 --> 00:00:00.210]   [
[00:00:00.210 --> 00:00:00.420]  M
[00:00:00.420 --> 00:00:01.020]  US
[00:00:01.020 --> 00:00:01.260]  IC
[00:00:01.260 --> 00:00:02.110]   PLAY
[00:00:02.110 --> 00:00:02.740]  ING
[00:00:02.740 --> 00:00:02.980]  ]
[00:00:02.980 --> 00:00:02.980]  
[00:00:02.980 --> 00:00:03.190]   ["""

if __name__ == "__main__":
    parse_text(test_case_1)
