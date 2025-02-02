import math
import random
from itertools import permutations
#1
def gram(grams):
    return 28.3495231* grams

#2
def gradus(f):
    return (5/9) * (f-32)

#3
def solve(numheads,numlegs):
    for chickens in range(numheads +1):
        rabbits = numheads - chickens
        if(chickens *2 + rabbits *4) == numlegs:
            return chickens,rabbits
    return None

#4
def prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i ==0:
            return False 
    return True

def filter(nums):
    return [num for num in nums if prime(num)]

#5
def sss(s):
    return ["".join(p) for p in permutations(s)]

#6
def reverse(sent):
    return " ".join(sent.split()[::-1])

#7
def has_33(nums):
    return any (nums[i]==3 and nums[i+3]==3 for i in range(len(nums)-1))

#8
def spy_game(nums):
    code=[0,0,7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return False
        return True

#9
def sphere(radius):
    return(4/3) * math.pi * radius**3

#10
def elem(l):
    unl=[]
    for item in l:
        if item not in unl:
            unl.append(item)
    return unl

#11
def palidrome(s):
    return s==s[::-1]

#12
def histogram(l):
    for num in l:
        print("*" * num)

#13
def guess_the_num():
    name=input("Hello! What is your name? ")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    num=random.randint(1,20)
    guess=0
    while True:
        gues= int(input("Take a guess.\n"))
        guess+=1
        if gues<num:
            print("Your guess is too low")
        elif gues>num:
            print("Your guess is too high")
        else:
            print(f"Good job, {name}! You guessed my number in {guess} guesses!")


if __name__ == "__main__":
    print("Ounces: ", gram(100))
    print("Celsius: ", gradus(98))
    print("Chickens and Rabbits: ", solve(35, 94))
    print("Prime numbers: ", filter([10, 15, 3, 5, 8, 13, 17, 20, 23, 29]))
    print("Permutations: ", sss("abc"))
    print("Reversed sentence: ", reverse("We are ready"))
    print("Has 33: ", has_33([1, 3, 3]))
    print("Spy game: ", spy_game([1, 2, 4, 0, 0, 7, 5]))
    print("Sphere volume: ", sphere(3))
    print("Unique elements: ", elem([1, 2, 2, 3, 4, 4, 5]))
    print("Palindrome check: ", palidrome("madam"))
    histogram([4, 9, 7])
