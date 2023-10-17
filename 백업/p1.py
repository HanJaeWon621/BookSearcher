import requests

url = 'https://jsonplaceholder.typicode.com/comments'
data = '{"username":"user1","password":"pass1"}'
headers = {"Content-Type":"application/json"}

response = requests.get(url, data=data, headers=headers)

print(response.json())