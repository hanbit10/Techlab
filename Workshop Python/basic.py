# x = input("insert input x:")
# y = input("insert input y:")
# print(x, "divided by", y)
# print("integer = ", int(x)//int(y))
# print("remainder = ", int(x)%int(y))

# def afunc(value):
#   y = value
#   x = int(y)
#   if(x%3 == 0 and x%5 == 0):
#     print("I am not cool")
#   elif(x%3 == 0 or x%5 == 0):
#     print("I am cool")
#   else:
#     print("not defined")

# def fizzbuzz(value):
#   y = value
#   x = int(y)
#   i = 1
#   while (i < x):   
#     if(i%3 == 0 and i%5 == 0):
#       print(i, "FizzBuzz")
#     elif(i%3 == 0):
#       print(i, "Fizz")
#     elif (i%5 == 0):
#       print(i, "Buzz")
#     else:
#       print(i, "not defined") 
#     i = i + 1

def estimate_pi(n):
  res = 0
  for i in range(0, n):
    temp = (((-1)**i)/(2*i + 1))
    res = res + temp
  print(4*res)

estimate_pi(21700)

