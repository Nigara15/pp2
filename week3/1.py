import math
#1
class stringss:
    def __init__(self):
        self.string=""
    def getstring(self):
        self.string=input()
    def printstring(self):
        print(self.string.upper())

#2
class shape:
    def area(self):
        return 0
    
class square(shape):
    def __init__(self,l):
        self.l=l
    def area(self):
        return self.l** 2
    
#3
class rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    
    def area(self):
        return self.l * self.w

#4
class points:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def show(self):
        print(f"points({self.x}, {self.y})")
    
    def move(self,a,b):
        self.a=a
        self.b=b

    def dist(self,c):
        return math.sqrt((self.a -self.c)** 2 + (self.b-self.c) ** 2)
    
#5
class account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposit(self, n):
        self.balance+=n
        print(f"Deposited {n}. New balance: {self.balance}")
    
    def withdraw (self,n):
        if n> self.balance:
            print("Insufficient balance")
        else:
            self.balance-=n
            print(f"Withdrew {n}. New balance: {self.balance}")

#6
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i ==0:
            return False 
        return True
    
numbers = [1, 3, 5, 10, 14, 27, 30, 33, 49]
prime_numbers = list(filter(lambda x:prime(x), numbers))
print("Prime numbers in the list:", prime_numbers)



if __name__ == "__main__":
    str_handler = stringss()
    str_handler.getstring()
    str_handler.printstring()

    sq=square(4)
    print(sq.area())

    rect = rectangle(4, 5)
    print(rect.area())

    p1 = points(2, 3)
    p2 = points(5, 7)
    p1.show()
    print(p1.dist(p2))

    acc = account("Nigara", 100)
    acc.deposit(50)
    acc.withdraw(30)
    acc.withdraw(200)
