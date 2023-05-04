import shutil
import os

# make a copy of the invoice to work with
img_directories =  ['validation', 'test', 'train']


for img_directory in img_directories:
    list_file = f'{img_directory}.txt'

    for filename in os.listdir(f"{img_directory}/images"):
        with open(list_file, 'a+', newline='') as file:
            file.write(f'./{img_directory}/images/{filename}')
            file.write('\n')
