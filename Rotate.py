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
    for image in images.iterdir():

        # load the image and show it
        img = cv2.imread(str(image))

        (h, w) = img.shape[:2] 
        (cX, cY) = (w // 2, h // 2) # image center for rotation

        for i in range(15):

            angle = 22.5*(i+1) # rotate our image by 22.5 degrees per iteration around the center of the image
            M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
            rotated = cv2.warpAffine(img, M, (w, h), borderValue = (0, 0, 0))

            path = Path(images / f"{str(int(image.stem)+(1+i)*1000000).zfill(8)}{image.suffix}")
            
            cv2.imwrite(str(path), rotated)

