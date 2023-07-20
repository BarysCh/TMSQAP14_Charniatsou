# Словари:
# 1 Создайте словарь, связав его с переменной school, и наполните его данными,
# которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б,
# 2б, 6а, 7в и т.д.).

school = {"1a": 22, "1b": 23, "2a": 19, "2b": 20, "3a": 18, "3b": 22, "4a": 24, "4b": 20, "5a": 25, "5b": 26}

# 2 Узнайте сколько человек в каком-нибудь классе.
print(school["3a"])
# 3 Представьте, что в школе произошли изменения, внесите их в словарь:
# ◦ в трех классах изменилось количество учащихся;

def edit_dictionary(x, y, z):
    """edits a value in a dictionary, adds new items to a dictionary"""
    x[y] = z

edit_dictionary(school, "1a", 21)

# ◦ в школе появилось два новых класса;
edit_dictionary(school, "1c", 24)
edit_dictionary(school, "3c", 20)


# ◦ в школе расформировали один из классов.
def remove_item_from_dict(x, y):
    """removes an item from a dictionary"""
    x.pop(y)

remove_item_from_dict(school, "1b")
# 4 Выведите содержимое словаря на экран.
print(school)
