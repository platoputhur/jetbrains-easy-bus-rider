import re

string = input()
# your code here
template = r"\+(\d{1})(-|\s)?(\d{3})(-|\s)?([\d\-\s]*)"
matched_groups = re.match(template, string)
if matched_groups is not None:
    print(f"Full number: {string}")
    print(f"Country code: {matched_groups.group(1)}")
    print(f"Area code: {matched_groups.group(3)}")
    print(f"Number: {matched_groups.group(5)}")
else:
    print("No match")
