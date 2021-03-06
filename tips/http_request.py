import requests

res = requests.get('https://developers.line.me/ja/docs/messaging-api/reference/')
print(dir(res))

print("======================================")
print("[req.content]")
print(res.content)
print("======================================")
print("[req.json]")
print(res.json)
print("======================================")
print("[req.iter_lines]")
print(res.iter_lines)
print("======================================")
print("[req.headers]")
print(res.headers)
print("======================================")
print("[req.encoding]")
print(res.encoding)
print("======================================")
print("[req.links]")
print(res.links)
print("======================================")
print("[req.status_code]")
print(res.status_code)
print("======================================")
print("[req.text]")
print(res.text)
print("======================================")
print("[req.url]")
print(res.url)
print("======================================")
