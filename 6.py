# Создайте функцию, которая принимает список слов
# и возвращает список слов, начинающихся с определенной буквы.


# var
words = []
letter = ""
sorted_words = []


# def
def right_letter(words, letter):
    for i in words:
        if i[0].lower() == letter.lower():
            sorted_words.append(i)
            print(i, ", ", end="", sep="")


# main
print("Enter some words(sep. by space): ")
words = input().split()
print("Enter required letter: ")
letter = str(input())
right_letter(words, letter)
