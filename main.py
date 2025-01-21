def sum_multiples_of_3_or_5(N):
    total = 0
    for i in range(1, N+1):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

N = int(input("Введите число N: "))
result = sum_multiples_of_3_or_5(N)
print(f"Сумма всех чисел от 1 до {N}, кратных 3 или 5: {result}")
