import re 

pets = input()
# your code here
pets_pattern = r'dog|cat|parrot|hamster'
result = re.findall(pets_pattern, pets, flags=re.IGNORECASE)
print(result)
