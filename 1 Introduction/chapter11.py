class PartyAnimal:
  x = 1
  name = ""
  def __init__(self, z):
    self.name = z
    print("This prints calling class with name: ", self.name)
  
  def party(self):
    self.x = self.x + 1
    print("So far", self.x)
    
    def __delitem__(self):
      print("I deleted something", self.x)

class FootballFan(PartyAnimal):
  points = 0
  def touchdown(self):
    self.points = self.points + 7
    self.party()
    print(self.name, "points", self.points)

an = PartyAnimal("Sally")

# an.party()
# an = 42
# print(an)
# print(an)

be = FootballFan("Jim")
be.party()
be.touchdown()