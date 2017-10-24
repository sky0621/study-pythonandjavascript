import requests

res = requests.get("https://demo.ckan.org/api/3/action/tag_list")
#print(res.json())
data = res.json()
print(data.keys())
