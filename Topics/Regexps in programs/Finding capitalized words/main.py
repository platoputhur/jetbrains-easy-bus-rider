import re

string = input()
# your code here
caps_pattern = r'[A-Z]\w+'
digits_pattern = r'\d+'
print(f"Capitalized words: {', '.join(re.findall(caps_pattern, string))}")
print(f"Digits: {', '.join(re.findall(digits_pattern, string))}")
