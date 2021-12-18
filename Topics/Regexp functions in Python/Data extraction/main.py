import re

string = input()
# your code
pattern = r"<START>([^(<END>).]*)<END>"
matched_string = re.findall(pattern, string, re.DOTALL)
print(matched_string[0])
