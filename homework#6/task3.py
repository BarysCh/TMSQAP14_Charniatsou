def square_numbers_in_file(file):
    """extracts numbers from a file, multiplies them by the power of two"""
    with open(file, "r") as f:
        content = f.readlines()
        arr = []
        for i in content:
            i = float(i)
            if i % 1 == 0:
                i = int(i)
            new_i = i ** 2
            arr.append(new_i)
        return arr


def write_numbers_into_file(file, numbers_list):
    """writes numbers into a file, with a separate line for each number"""
    with open(file, "w") as f:
        for i in numbers_list:
            f.write(("%s\n" % i))


numbers_file = "file5.txt"

num_list = square_numbers_in_file(numbers_file)

write_numbers_into_file(numbers_file, num_list)










