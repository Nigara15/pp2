#1
import time
import math
from functools import reduce 
import operator

def mul(num):
    return reduce(operator.mul,num,1)

num=[2,3,4,5]
print(mul(num))

#2
def count(s):
    upper=sum(1 for char in s if char.isupper())
    lower=sum(1 for char in s if char.islower())
    return {"uppercase" : upper,"lowercase" : lower}

text="Nigara krutaya"
print(count(text))

#3
def palid(s):
    return s==s[::-1]

n=input()
print(palid(n))

#4
def sqrt(num,d):
    time.sleep(d/1000)
    return math.sqrt(num)

num=2500
d=2123
res=sqrt(num,d)
print(f"square root of {num} after {d} milliseconds is {res}")

#5
def truee(t):
    return all(t)

print(truee((True, True, True)))
print(truee((False, True, True)))
