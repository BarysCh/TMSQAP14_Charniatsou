# Работа с переменными:
# 1 Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
var_int = 10
var_float = 8.4
var_str = "No"

# 2 Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза,
# результат свяжите с переменной big_int.


def multiply(x, y=3.5):
    """Multiplies a variable by 3.5"""
    return x * y


big_int = multiply(var_int)

# 3 Измените значение, хранимое в переменной var_float, уменьшив его на единицу,
# результат свяжите с той же переменной.


def subtract(x):
    """Subtracts one from a variable"""
    return x - 1


var_float = subtract(var_float)

# 4 Разделите var_int на var_float, а затем big_int на var_float. Результат данных
# выражений не привязывайте ни к каким переменным.


def divide(x,y):
    """divides a variable by another variable"""
    return x / y


divide(var_int, var_float)
divide(big_int, var_float)

# 5 Измените значение переменной var_str на "NoNoYesYesYes". При формировании
# нового значения используйте операции конкатенации (+) и повторения строки (*).
var_str = multiply(var_str, 2) + multiply("Yes", 3)


# 6 Выведите значения всех переменных.
print(var_int, var_float, big_int, var_str)
