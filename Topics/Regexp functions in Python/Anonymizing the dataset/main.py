import re

string = input()
# your code
author_pattern = r"^@[a-zA-Z_0-9]*"
handles_patter = r"@[a-zA-Z_0-9]*"
replaced_string = re.sub(author_pattern, '<AUTHOR>', string, 1)
replaced_string = re.sub(handles_patter, '<HANDLE>', replaced_string, 0)
print(replaced_string)
