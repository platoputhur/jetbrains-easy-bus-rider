import re

string = input()
# your code here
template = r"(Good\s\w+)"
match = re.match(template, string)
print(match.group(1) if match else "No greeting!")
