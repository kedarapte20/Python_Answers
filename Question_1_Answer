import requests
import json
response = requests.get("https://my-json-server.typicode.com/typicode/demo/posts")
json_data1= json.loads(response.text)
response = requests.get("https://my-json-server.typicode.com/typicode/demo/comments")
json_data2 = json.loads(response.text)
k = []
for i in json_data2:
    k.append(i["id"])
a = 0
for i in json_data1:
    for j in k:
        if i["id"] == j:
            i.__setitem__("body",json_data2[a]["body"])
            a += 1
print(json.dumps(json_data1))
