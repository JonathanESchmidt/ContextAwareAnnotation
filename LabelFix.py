import shutil
import os
from pathlib import Path

# make a copy of the invoice to work with
img_directories =  ['validation', 'test', 'train']


for img_directory in img_directories:
    oldPath = Path(f"{img_directory}/labels")
    newPath = Path(f"{img_directory}/newlabels")

    for label in oldPath.iterdir():

        content = Path(label).read_text(encoding="utf-8")
        boxes = [line for line in content.splitlines()]
        path = newPath / label.name

        print(path)
        for box in boxes:
            print(box)
            if len(box):   
                numbers = box.split(',')
                ID = int(numbers[0]) 
                x = float(numbers[1])
                y = float(numbers[2])
                width = float(numbers[3])
                height = float(numbers[4])
                print(f'{ID} {x} {y} {width} {height}')
                path.write_text(f'{ID} {x} {y} {width} {height}\n')
                
            else:
                path.write_text('\n')
                
