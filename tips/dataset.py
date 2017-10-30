import dataset

db = dataset.connect('sqlite:///data/nobel_prize.db')

wtable = db['winners']
winners = wtable.find()
winners = list(winners)
print(winners)
