# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())
