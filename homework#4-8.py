# Цикл for
# 1
# Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
# включительно.

def find_sum(x, y):
    """finds the sum of all numbers in the range from one number through another"""
    total = 0
    for i in range(x, y+1):
        total += i
    return total


print(find_sum(1, 8))

# 2
# Найти сумму всех натуральных чисел в от A до B


def find_sum1(x, y):
    """finds the sum of all numbers in the range between two given natural numbers"""
    total = 0
    if x >= 0 and y >= 0:
        for i in range(x, y):
            total += i
        return total
    else:
        pass


print(find_sum1(1, 5))

# 3
# Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.
numbers = [3, -4, 5, 9, -8, 13, 6, -1, 10, 22]


def calculate(x):
    """multiplies all positive numbers, finds the sum and quantity of all negative numbers"""
    result1 = 1
    result2 = 0
    result3 = 0
    for i in x:
        if i > 0:
            result1 = result1 * i
        if i < 0:
            result2 += i
            result3 += 1
    return result1, result2, result3


print(calculate(numbers))

# 4
# Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17

results = {"Бекиш Александр": 21.07, "Будник Алексей": 20.34, "Гребень Анастасия": 22.12,
          "Давидович Татьяна": 30, "Дешук Дмитирий": 24.01, "Казак Анна": 28.17}


def find_best_result(x):
    """returns the best result in a race"""
    best_result = min(x.values())
    for key, value in x.items():
        if value == best_result:
            return key, value


print(find_best_result(results))

# 5
# Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5 Напишите программу, которая будет выводить
# уникальное число

numbers = [1, 5, 2, 9, 2, 9, 1]


def find_unique_number(x):
    """finds unique numbers in a list"""
    for i in x:
        if x.count(i) == 1:
            return i


print(find_unique_number(numbers))
