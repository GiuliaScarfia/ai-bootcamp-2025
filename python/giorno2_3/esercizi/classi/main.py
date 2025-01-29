class City:
    def __init__(self, name, pop):
        self.name = name
        self.pop = pop

class Region:
    def __init__(self, name):
        self.name=name
        self.cities=[]
    def add(self,city):
        self.cities.append(city)
    @property
    def pop(self):
        return sum(city.pop for city in self.cities)

class Country:
    def __init__(self, name):
        self.name=name
        self.regions = []
    def add(self, region):
        self.regions.append(region)
    @property
    def pop(self):
        return sum(region.pop for region in self.regions)
    @property
    def most_populous_city(self):
        all_cities=[city for region in self.regions for city in region.cities]
        return max(all_cities, key=lambda city: city.pop)

italy = Country("Italy")
assert italy.name == "Italy"

sicily = Region("Sicily")
sicily.add(City("Catania", pop=300_000))
sicily.add(City("Palermo", pop=600_000))

italy.add(sicily)

assert sicily.pop == 900_000

calabria = Region("Calabria")
calabria.add(City("Reggio Calabria", pop=170_000))

italy.add(calabria)

assert italy.pop == 1_070_000
assert italy.most_populous_city.name == "Palermo"