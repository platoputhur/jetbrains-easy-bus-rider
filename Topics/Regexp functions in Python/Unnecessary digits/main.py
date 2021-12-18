import re       
names = input()
# your code here
pattern = r"\d+"
names_list = re.split(pattern, names)
print(names_list)
