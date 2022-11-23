# Развернутое решение
word = input("Введите слово: ")
word_len = len(word)

for i in range(0, word_len, 2):
    print(word[i])

# Короткое решение
[print(letter) for letter in input("Введите слово: ")[::2]]
