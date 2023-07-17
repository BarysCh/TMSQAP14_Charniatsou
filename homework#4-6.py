# 1
# Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
def string_to_list(x):
    """converts a string to a list"""
    return x.split()


string1 = "Robin Singh"
string2 = "I love arrays they are my favorite"

print(string_to_list(string1))
print(string_to_list(string2))

# 2
# Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”


def convert_into_string(x):
    "converts a list into a string"
    return " ".join(x)


lst = ["Ivan", "Ivanou"]
string1 = "Minsk"
string2 = "Belarus"
print("Привет, " + convert_into_string(lst) + "! Добро пожаловать в " + string1 + " " + string2)

# 3
# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"
lst2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]

print(convert_into_string(lst2))

# 4
# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def edit_list(x, y, z):
    """edits a list"""
    x[y] = z
    return x


print(edit_list(lst2, 2, "new value"))
# 5
# Есть 2 словаря

# Необходимо их объединить по ключам, а значения ключей поместить в список, если у
# одного словаря есть ключ "а", а у другого нету, то поставить значение None на
# соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}


def merge_dictionaries(x, y):
    """merges dictionaries into a new one, keeps all values for the common keys"""
    new_dict = {**x, **y}
    for key in x:
        if key not in y:
            new_dict[key] = [x[key], None]
        else:
            new_dict[key] = [x[key], y[key]]
    for key in y:
        if key not in x:
            new_dict[key] = [None, y[key]]
        else:
            pass

    return new_dict


print(merge_dictionaries(a, b))

