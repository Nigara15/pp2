import math 
#1
def radians(degree):
    return round(degree*(math.pi /180,6))

#2
def trapezoid(h,b1,b2):
    return round((b1+b2)* h/2,2)

#3
def polygon(n,s):
    return round((n* s**2)/(4* math.tan(math.pi/n),2))

#4
def parallelogram(b,h):
    return round(b * h,2)

print(radians(15))
print(trapezoid(5, 5, 6))
print(polygon(4, 25))
print(parallelogram(5, 6))