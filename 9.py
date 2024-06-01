# Напишите функцию, которая принимает список чисел и возвращает новый список с квадратами этих чисел.

# var
numbers = []
square_mnumbers = []

# main
print("Enter numbers(sep. by space): ")
numbers = input().split()

for i in numbers:
    square_mnumbers.append(int(i)**2)

print(square_mnumbers)
