import os

directory = 'C:/'

contents = os.listdir(directory)

for item in contents:
    print(item)