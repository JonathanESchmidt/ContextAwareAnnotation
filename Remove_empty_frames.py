import numpy as np
import argparse
from pathlib import Path
import cv2
import time


if __name__ == '__main__':

    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_template', type=str,
                        default="./template.png", help='image to compare to others')
    parser.add_argument('--img_directory', type=str, default="./images",
                        help='path to folder with images to be annotated')

    args = parser.parse_args()

    template = cv2.imread(str(Path(args.img_template)))
    images = Path(args.img_directory)

    image_count = 0

    for image in images.iterdir():

        img = cv2.imread(str(image))

        if np.array_equal(img, template):  # test if same shape, same elements values
            image.unlink()
            image_count += 1

    print(f"Removed {image_count} images in {time.time()-start_time} seconds")
