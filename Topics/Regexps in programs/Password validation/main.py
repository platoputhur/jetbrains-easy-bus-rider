import re

password = input()
# your code here
password_pattern = r'\w{6,15}'
if re.match(password_pattern, password, flags=re.ASCII):
    print("Thank you!")
else:
    print("Error!")