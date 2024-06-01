# Создайте функцию, которая принимает строку и возвращает ее в обратном порядке.

# var
string = ""
reverse_string = ""


# def
def reverse(string):
    return string[-1::-1]


# main
print("Enter string: ")
string = input()
reverse_string = reverse(string)
print(reverse_string)
