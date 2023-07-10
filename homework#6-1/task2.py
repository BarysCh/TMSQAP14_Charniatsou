#Создать lambda функцию, которая принимает на вход список имен и выводит их в формате 'Hello
# {name}' в другой список

list_of_names = ["Ivan", "Nickolay", "Piotr", "Olga", "Tanya"]

greeting_list = lambda name_list: list(f"Hello, {name}" for name in name_list)

print(greeting_list(list_of_names))
