# Напишите функцию, которая принимает список чисел и возвращает только уникальные элементы.


# var
numbers = []
list_length = 0


# main
print("Enter some numbers(sep. by space): ")
numbers = input().split()

for i in numbers:
    if numbers.count(i) > 1:
        while not (numbers.count(i) == 0):
            numbers.remove(i)

print(numbers)
