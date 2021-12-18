import json


# write your code here
json_string = input()
json_obj = json.loads(json_string)
print(type(json_obj))
print(json_obj)