import pickle


def write_into_bin_file(bin_file, num_list):
    """writes a list into a bin. file"""
    with open(bin_file, "wb") as f:
        pickle.dump(num_list, f)


def load_from_bin_file(bin_file):
    """loads data from a bin.file"""
    with open(bin_file, "rb") as f:
        data = pickle.load(f)
        return data


arr1 = [10,20,30,40]
arr2 = [5,10,15,20]
file1 = "binfile_1.bin"
file2 = "binfile_2.bin"

write_into_bin_file(file1, arr1)
write_into_bin_file(file2, arr2)
data1 = load_from_bin_file(file1)
data2 = load_from_bin_file(file2)
write_into_bin_file(file1, data2)
write_into_bin_file(file2, data1)