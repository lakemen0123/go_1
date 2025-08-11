def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

try:
    n = int(input("Сколько чисел Фибоначчи вывести? "))
    if n <= 0:
        print("Введите число больше 0!")
    else:
        print(f"Числа Фибоначчи: {fibonacci(n)}")
except ValueError:
    print("Введите целое число!")