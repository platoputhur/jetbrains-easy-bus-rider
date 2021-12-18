import re

string = input()
# your code here
pattern = r'[0-3]{1}[0-9]{1}/[0-1]{1}[0-9]{1}/\d{4}'
if re.match(pattern, string):
    print(True)
else:
    print(False)