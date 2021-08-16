import requests
import json
json_data = []
for i in range(1,13):
    response = requests.get(f"https://reqres.in/api/users?page={i}")
    json_data.append(json.loads(response.text))
print(len(json_data))
