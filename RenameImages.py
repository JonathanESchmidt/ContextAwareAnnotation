import argparse
from pathlib import Path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_directory', type=str, default="./images",
                        help='path to folder with images to be annotated')
    parser.add_argument('--record_number', type=int, default="0",
                        help='path to folder with images to be annotated')

    args = parser.parse_args()

    record_number = 6

    folders = [r"C:\Users\Jonathan\Downloads\DividedBags\random_walking\images"]

    for folder in folders:
        images = Path(folder)
        for image in images.iterdir():

            path = Path(
                images / f"{str(int(image.stem)+(record_number)*100000).zfill(8)}{image.suffix}")
            image.rename(path)
