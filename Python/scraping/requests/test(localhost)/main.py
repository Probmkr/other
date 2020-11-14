import requests

URL = input()

a = requests.get(URL)
print(a.content.decode('utf-8'))