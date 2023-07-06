import pickle

arr = [10,20,30,40]
arr1 = [5,10,15,20]

with open("binfile_1.bin", "wb") as file:
    pickle.dump(arr, file)

with open("binfile_2.bin", "wb") as file:
    pickle.dump(arr1, file)

with open("binfile_1.bin", "rb") as file:
    data = pickle.load(file)

with open("binfile_2.bin", "rb") as file:
    data_1 = pickle.load(file)

with open("binfile_1.bin", "wb") as file:
    pickle.dump(data_1, file)

with open("binfile_2.bin", "wb") as file:
    pickle.dump(data, file)

