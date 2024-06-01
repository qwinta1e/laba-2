# Создайте программу, которая проверяет, является ли введенная пользователем строка палиндромом

# var
word = ""
flag = True

# main
print("Enter word: ")
word = input()
for i in range(int(len(word)/2)):
    if word[i] == word[-i-1]:
        continue
    else:
        print("This word is not a palindrome")
        flag = False
        break

if flag == True:
    print("This word is a palimdrome")
