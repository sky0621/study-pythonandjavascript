class Citizen(object):
    # インスタンス作成時に呼ばれる
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def print_details(self):
        print('Citizen %s from %s'%(self.name, self.country))

c = Citizen('Groucho M.', 'Freedonia')
c.print_details()

# Citizenを継承
class Winner(Citizen):
    def __init__(self, name, country, category, year):
        # Winnerをselfとして使って、親クラス「Citizen」の__init__を再利用する
        super(Winner, self).__init__(name, country)
        self.category = category
        self.year = year

    def print_details(self):
        print('Nobel winner %s from %s, category %s, year %s'\
              %(self.name, self.country, self.category, str(self.year)))

w = Winner('Albert E.', 'Switzerland', 'Physics', 1921)
w.print_details()
