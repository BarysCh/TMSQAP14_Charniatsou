# 1.2 Определить переменные всех типов и выведите их на экран
a = 6
b = 6.5
c = "short string"
d = a != b
e = {}
f = {"a", "b", "c"}
g = []
j = ()
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(j))


#1.3 Найти значение выражений
x = 17 / 2 * 3 + 2
x = 27.5
x = 2 + 17 / 2 * 3
x = 27.5
x = 19 % 4 + 15 / 2 * 3
x = 25.5
x = (15 + 6) - 10 * 4
x = -19
x = 17 / 2 % 2 * 3**3
x = 13.5

#1.4 Создать три переменные, содержащие возраст трех ближайших соседей, найти сумму и вывести ее на экран.
#Создать еще одну переменную равную среднему арифметическому возрасту, и вывести это значение на экран.

sasha_age = 37
petya_age = 44
nastya_age = 12
total = sasha_age + petya_age + nastya_age
print(total)

average_age = total / 3
print(average_age)

#1 Привести к целому типу -1.6, 2.99
x = round(1.6)
y = round(2.99)
print(x, y)

#2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
txt = "www.my_site.com#about"
new_txt = txt.replace("#", "/")
print(new_txt)

#3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
first_string = "stroka"
second_string = "ing"
new_string = first_string + second_string
print(new_string)

#4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
name = "Ivanou Ivan"
ls = name.split(" ")
ls[0], ls[1] = ls[1], ls[0]
new_name = " ".join(ls)
print(new_name)

#5 Напишите программу которая удаляет пробел в начале, в конце строки
x = " my string "
new_x = x.strip()
print(new_x)

#6 Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {"1a": 22, "1b": 23, "2a": 19, "2b": 20, "3a": 18, "3b": 22, "4a": 24, "4b": 20, "5a": 25, "5b": 26}

#7 Создайте список и извлеките из него списка второй элемент
my_list = [1, 2, 3, 4, 5]
x = my_list.pop(1)
print(x)

#8 Вывести входит ли строка1 в строку2 (пример: employ и employment )
string1 = "employ"
string2 = "employment"
print(string2.find(string1))

#9 Вывести нужные символы
x = "My name is Agent Smith"
print(x[1]) #y
print(x[3:16:3]) #nesgt