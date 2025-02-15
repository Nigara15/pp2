#1
def square(N):
    for i in range(N + 1):
        yield i ** 2

#2
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

#3
def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

print( list(square(5)))
n = int(input())
print("Even numbers:", ", ".join(map(str, even_numbers(n))))

print( list(divisible(20)))

for value in squares(3, 7):
    print(value)

for value in countdown(5):
    print(value)