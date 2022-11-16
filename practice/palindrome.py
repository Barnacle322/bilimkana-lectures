"""
Напишите код, который будет выводить True, если слово
палиндром(читается в две стороны одинаково), False, если нет. 
"""

def isPalindrome(word: str) -> bool:
    # 1. Перевернуть слово 
    # 2. Сравнить слова
    # 3. Вывести либо False либо True

    # Решение 1
    # if word[::-1] == word:
    #     return True
    # else:
    #     return False

    # Решение 2
    return word[::-1] == word
        

print(isPalindrome("аргентинаманитнегра"))