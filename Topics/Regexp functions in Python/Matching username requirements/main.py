import re
username = input()
pattern = r"^[A-Za-z]{1}\w+$"
if not re.match(pattern, username):
    print("Oops! The username has to start with a letter.")
else:
    print("Thank you!")
    