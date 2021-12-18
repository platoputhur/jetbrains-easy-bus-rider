import re

template = r'are you ready??.?.?'
string = input()
match = re.match(template, string)
if match:
    print(match.end() - match.start())
else:
    print(0)
