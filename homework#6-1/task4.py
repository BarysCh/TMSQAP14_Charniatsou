#Необходимоо составить список чисел, которые указывают на длину слов в строке sentence =
# "thequick brown fox jumps over the lazy dog", но только если слово не "the" с обработкой исключений

sentence = "thequick brown fox jumps over the lazy dog"


def word_length_generator(my_string):
    """takes a string and yields the length of words in it, except for 'the' word"""
    num_list = []
    new_string = my_string.split()
    for i in new_string:
        try:
            if i == "the":
                raise ValueError
            num_list.append(len(i))
        except ValueError:
            continue
    yield num_list


my_generator = word_length_generator(sentence)

print(next(my_generator))




