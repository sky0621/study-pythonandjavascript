import requests

res = requests.get("https://en.wikipedia.org/wiki/Nobel_Prize")
print(dir(res))

print(res.status_code)
print(res.headers)