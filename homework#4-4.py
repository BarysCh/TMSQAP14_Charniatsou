# Логические операции:
# 1 Присвойте двум переменным любые числовые значения.
var1 = 5
var2 = 12
# 2 Составьте четыре сложных логических выражения с помощью оператора and, два из
# которых должны давать истину, а два других - ложь.
print(var1 > 2 and var2 > 2)
print(var1 < 6 and var2 > 6)
print(var1 > 6 and var2 > 6)
print(var1 < 4 and var2 > 13)

# 3 Аналогично выполните п. 2, но уже используя оператор or.
print(var1 > 2 or var2 > 2)
print(var1 < 6 or var2 < 6)
print(var1 > 6 or var2 < 6)
print(var1 == 4 or var2 == 13)
# 4 Попробуйте использовать в сложных логических выражениях работу с переменными
# строкового типа.
string = "Ivan"
string1 = "Alesya"
print((string or string1) in "Alesya")
print((string1 or string) in "Alesya")