def write_into_file(file, content):
    """opens a txt.file, writes content into it"""
    with open(file, "w") as f:
        f.write(content)


def read_file(file, *args):
    with open(file, "r") as f:
        content = f.readline()
        if len(content) < 3:
            print("Error")
        else:
            for arg in args:
                print(content[arg])


new_file = "file1.txt"
file_content = "12345"


write_into_file(new_file, file_content)
read_file(new_file, 0, 1, -2, -1)





