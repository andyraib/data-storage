import requests
r = requests.get(url='https://api.github.com/users/andyraib/repos')
print(r.json())
