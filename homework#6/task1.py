with open("file1.txt", "w") as f:
    f.write("12345")

with open("file1.txt", "r") as f:
    content = f.readline()
    if len(content) < 3:
        print("Error")
    else:
        print(content[0], content[1], content[-2], content[-1])

