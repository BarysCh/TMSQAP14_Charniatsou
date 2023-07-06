with open("file2.txt", "w") as f:
    f.write("123456")

with open("file3.txt", "w") as f:
    f.write("")

with open("file4.txt", "w") as f:
    f.write("")

with open("file2.txt", "r") as f:
    content = f.readline()
    for i in content:
        i = int(i)
        if i % 2 == 0:
            with open("file3.txt", "a") as file:
                file.write(str(i))
        else:
            with open("file4.txt", "a") as file:
                file.write(str(i))

