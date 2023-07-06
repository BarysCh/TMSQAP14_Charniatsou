with open("file5.txt", "r") as file:
    content = file.readlines()
    arr = []
    for i in content:
        i = float(i)
        if i % 1 == 0:
            i = int(i)
        new_i = i ** 2
        arr.append(new_i)

with open("file5.txt", "w") as file:
    for i in arr:
        file.write(("%s\n" % i))













