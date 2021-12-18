# write your code here
import json

with open('users.json') as users:
    loaded_json = json.load(users)
    users_list = loaded_json['users']
    print(len(users_list))
