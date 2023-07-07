def write_into_file(file, content):
    """writes content into a txt. file"""
    with open(file, "w") as f:
        f.write(content)


def distribute_content(file,file_1, file_2):
    """distributes content of one file into two others"""
    with open(file, "r") as f:
        content = f.readline()
        for i in content:
            i = int(i)
            if i % 2 == 0:
                with open(file_1, "a") as f:
                    f.write(str(i))
            else:
                with open(file_2, "a") as f:
                    f.write(str(i))


new_file = "file2.txt"
file_content = "123456"
file1 = "file3.txt"
file2 = "file4.txt"
new_file_content = ""

write_into_file(new_file, file_content)
write_into_file(file1, new_file_content)
write_into_file(file2, new_file_content)
distribute_content(new_file, file1, file2)
