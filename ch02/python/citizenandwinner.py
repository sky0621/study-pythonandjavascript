class Citizen(object):
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def print_details(self):
        print('Citizen %s from %s'%(self.name, self.country))

c = Citizen('Groucho M.', 'Freedonia')
c.print_details()
