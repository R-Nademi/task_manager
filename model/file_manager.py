import os
import pickle


file_name = "task.dat"


def check_file():
    return os.path.exists(file_name)


def read_from_file():
    if check_file():
        file = open(file_name, "rb")
        data_list = pickle.load(file)
        file.close()
        return data_list
    else:
        file = open(file_name, "wb")
        file.close()
        return []

def write_to_file(data_list):
    file = open(file_name, "wb")
    pickle.dump(data_list, file)
    file.close()


