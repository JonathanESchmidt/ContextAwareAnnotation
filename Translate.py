import numpy as np
import argparse
from pathlib import Path
import cv2


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_directory', type=str, default="./images",
                        help='path to folder with images to be annotated')

    args = parser.parse_args()

    images = Path(args.img_directory)

    translations = [[-20, 0], # 1 meter left
                    [0, -20], # 1 meter up
                    [20, 0],  # 1 meter right
                    [0, 20],  # 1 meter down
                    [-10, 0], # ½ meter left
                    [0, -10], # ½ meter up
                    [10, 0],  # ½ meter right
                    [0, 10]]  # ½ meter up
    for image in images.iterdir():

        # load the image and show it
        img = cv2.imread(str(image))

        (h, w) = img.shape[:2] 
        (cX, cY) = (w // 2, h // 2) # image center for rotation

        for i, translation in enumerate(translations):
            
            print(translation[0])

            # shift the image 25 pixels to the right and 50 pixels down
            M = np.float32([[1, 0, translation[0]], [0, 1, translation[1]]])

            translated = cv2.warpAffine(img, M, (w, h), borderValue = (0, 0, 0))

            path = Path(images / f"{str(int(image.stem)+(1+i)*1000000).zfill(8)}{image.suffix}")
            cv2.imwrite(str(path), translated)
