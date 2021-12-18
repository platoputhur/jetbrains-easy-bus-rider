import re

string = input()
# your code here
pattern = r'(ou)'
result = re.sub(pattern, "o", string, flags=re.IGNORECASE, count=0)
print(result)

