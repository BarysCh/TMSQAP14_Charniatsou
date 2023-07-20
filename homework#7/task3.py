number_names = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
                8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
                14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
                19: "nineteen"}


def sort_numbers(numbers):
    """takes numbers as an argument and sorts them in the alphabetical order depending on their names"""
    numbers_list = map(int, numbers.split(" "))
    sorted_number_names = sorted([number_names[number] for number in numbers_list])
    final_list = []
    for i in range(len(sorted_number_names)):
        for key, value in number_names.items():
            if value == sorted_number_names[i]:
                final_list.append(key)

    return " ".join(map(str, final_list))


numbers = "1 2 6 8 9"
result = sort_numbers(numbers)
print(result)

