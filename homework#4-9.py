# Цикл while
# 1
# Дано число N. Найти произведение всех чисел от 0 до N.

def multiply_numbers(x, y):
    "multiplies all numbers in the range between two numbers"
    result = 1
    while x < y:
        result = result * x
        x += 1
    return result


print(multiply_numbers(0, 6))
# 2
# Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
# увеличивается втрое. Через сколько лет площадь первых сортов будет
# составлять меньше 10% от площади вторых сортов.


def find_year_count(s1, s2):
    """returns the number of years needed for one area to become less than 10% of the other area"""
    year_count = 0
    while s1 >= 0.1 * s2:
        s1 *= 2
        s2 *= 3
        year_count += 1
    return year_count


print(find_year_count(1, 2))

# 3
# Дано целое число N (>0). Используя операции деления нацело и взятия
# остатка от деления, найти количество и сумму его цифр.


def count_digits(n):
    """returns the number of digits in a number and their sum"""
    count = 0
    sum_of_digits = 0
    while n != 0:
        count += 1
        modul_value = n % 10
        sum_of_digits = sum_of_digits + modul_value
        n //= 10
    return count, sum_of_digits


print(count_digits(112))
# 4
# Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
# внука. И сколько при этом лет будет деду и внуку.


def count_years(m, n):
    """returns the number of years needed for one person to become twice as old as another one"""
    count = 0
    while m / 2 != n:
        count += 1
        m += 1
        n += 1
    return count, m, n


print(count_years(62, 1))
