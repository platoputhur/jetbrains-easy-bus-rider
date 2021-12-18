import re

string = input()
# your code here
result = re.search(r'(?<=-).*', string)
print(result.group())
