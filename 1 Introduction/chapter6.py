# aList = [1, 2, 3, 4, 5, 6]

# aList = list()

# for i in range(0, 5):
#   aList.append(i+1)

# print(sum(aList[:3]))

# line = "hello, this is, hanbit,well"

# print(line.split(','))

# first_dic = dict()
# first_dic['hello'] = 2

# print(first_dic['hello'])

counts = dict()
names = ['csev', 'cwen', 'hanbit', 'hanbit']

#the parameter get(name, 2) only sets the default of the value
for name in names:
  counts[name] = counts.get(name, 2) + 1



for i in counts:
  print(i)

print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())

for k,v in counts.items():
  if (k == "hanbit"):
    print("this is hanbit")
    

c = {'a':10, 'b':1, 'c':22}

#it sorts with the value instead of the keys

print(sorted([(v, k) for k,v in c.items()]))
