# Строки:
# 1 Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# Извлеките из строки первый символ, затем последний, третий с начала и третий с
# конца. Измерьте длину вашей строки.
string1 = "Charniatsou"


def change_string(x):
    """changes a string"""
    x = x[1:]
    x = x[:-1]
    x = x.replace(x[1], "", 1)
    x = x.replace(x[-2], "", 1)
    return x


print(len(change_string(string1)))
print(change_string(string1))

# 2 Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
# нее следующие срезы:
last_name = "Charniatsou"
# первые восемь символов


def shorten_string(x, y):
    """shortens a string to a certain number of symbols"""
    return x[:y]


shorten_string(last_name, 8)

# четыре символа из центра строки


def four_symbol_string(x, y, z):
    """reduces a string to several symbols from the middle"""
    return x[y:z]


four_symbol_string(last_name, 4, 8)

# символы с индексами кратными трем


def divisible_symbol_string(x, y):
    """reduces a string to symbols divisible by a certain number"""
    return x[y::y]


divisible_symbol_string(last_name, 3)
# переверните строку


def reverse_string(x):
    """reverses a string"""
    return x[::-1]


reverse_string(last_name)

# 3 Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте
# ваше имя.


def replace_word(x, y, z):
    """replaces a word in a string"""
    return x[:y] + z


string = "my name is name"
new_string = replace_word(string, 11, "Boris")
print(new_string)

# 4 Есть строка: test_tring = "Hello world!", необходимо
test_string = "Hello world!"
# напечатать на каком месте находится буква w
print(test_string.index("w"))
# кол-во букв l
print(test_string.count("l"))
# Проверить начинается ли строка с подстроки: “Hello”
print(test_string.startswith("Hello"))
# Проверить заканчивается ли строка подстрокой: “qwe”
print(test_string.endswith("qwe"))