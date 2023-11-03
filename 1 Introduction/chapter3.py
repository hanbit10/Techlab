print(max('Hellow world'))
# print(int('hello'))

#Lambda function
# def double(n):
#   return n*2

#lambda is anonymus function
double = lambda n:n*2
max = lambda a,b: a if a > b else b

print(max(10, 23))

names = ["Alan", "Gregory", "Zlatan", "Jonas", "Tom", "Augustine"]
names.sort(key = lambda x:len(x))
print(names)