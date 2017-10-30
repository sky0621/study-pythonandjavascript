import json

with open('data/dummy.json') as f:
    nobel_winners = json.load(f)
    print(nobel_winners)
