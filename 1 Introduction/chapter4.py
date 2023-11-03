# while True:
#   line = input('> ')
#   if line[0] == '#' :
#     continue
#   if line == 'done' :
#     break
#   print(line)
# print('Done!')

# #definite loops
for i in reversed("hello"):
  print (i)
  
# #loop idioms are like patterns
# largest_so_far = -1
# for num in [9, 41, 23, 3, 76, 14]:
#   if num > largest_so_far:
#     largest_so_far = num
#   print(largest_so_far)

# print("largest: ", largest_so_far)

found = False
print("Find value 3")
for value in [9, 41, 12, 3, 74, 14] :
  if value == 3:
    found = True

print(found)

smallest = None
for num in [9, 41, 23, 3, 76, 14]:
  if smallest is None:
    smallest = num
  if num < smallest:
    smallest = num
  print(smallest)

print("smallest: ", smallest)