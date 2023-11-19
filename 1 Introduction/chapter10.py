# mylist = ["apples", "bears", "oranges"]\
  

# for x, element in enumerate(mylist):
#   if x == 1:
#     print(element)
    
materials = ["a", "c", "d", "e", "s"]

materials.sort(reverse=True)
print(materials)

planets = [("a", 23, 1000),
             ("c", 13, 1313),
             ("d", 15, 1411),
             ("e", 24, 1311),
             ("s", 14, 1313)]

size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)

zipping = list(zip(materials, planets))
print(zipping)