import re


# put your regex in the variable template
template = r"Scaramouch."
string = input()
match = re.match(template, string)
print("Match") if match else print("No match")
