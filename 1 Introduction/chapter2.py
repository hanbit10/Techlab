# x = 11
# if x < 10:
#   print('Smaller')
# if x > 20:
#   print('Bigger')
  
# print('Finis')

# astr = 'Hello Bob'
# try:
#   istr = int(astr)
# except:
#   istr = -1
  
# astr = '123'
# try:
#   istr = int(astr)
# except:
# print('istr: ', istr)
#   istr = -1
  

rawstr = input('Enter number: ')
try:
  ival = int(rawstr)
except:
  ival = -1

if ival > 0:
  print('Nice work')
else:
  print('Not a number')