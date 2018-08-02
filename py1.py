print('hello world')

x=5.0/2
print(x)

if x>3:
    print("small")
else:
    print('big')

array=[1,1,2,3,5,8]
for val in array:
    print(val)

sum=0

position=0

while position<len(array):
    sum = sum + array[position]
    position= position + 1
    print(sum)

hash = {'a':125637, 'b':43876}
print(hash)
sum = 0

for key in hash:
    sum =sum+hash[key]

print(sum)

fib ={0:1, 1:1, 2:2, 3:3, 4:5, 5:8}
for key in fib:
    print(fib[key])
import person
me = person.Person()
print(me.name)
me.name = 'jkj'
print(me.name)
you = person.Person()
print(you.name)
you.age = 60

homo = person.Human('sap',58)
print(homo.name)
homo.older()

import pygame
print(dir(pygame))

def fib(nth_term):
    if nth_term == 1 or nth_term == 2:
        return 1
    return fib(nth_term - 1) + fib(nth_term-2)
print(fib(10))

def fib2(nth_term):
    if nth_term == 1 or nth_term == 2:
        return 1
    n = 3
    fibnminus2 =1
    fibnminus1 = 1
    while (n < nth_term):
        fibn = fibnminus1 + fibnminus2
        fibnminus2 = fibnminus1
        fibnminus1 = fibn
        n = n + 1
    return fibnminus1 + fibnminus2
print(fib2(100))
