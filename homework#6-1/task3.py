#Напишите генератор, который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6,
# 12.7] и возвращает новый список только с положительными числами

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


def positive_number_generator(num_list):
    """takes a list of numbers and yields only positive numbers out of that list"""
    new_num_list = []
    for number in num_list:
        if number > 0:
            new_num_list.append(number)
    yield new_num_list


my_generator = positive_number_generator(numbers)

print(next(my_generator))

