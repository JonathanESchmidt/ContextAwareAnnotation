import cv2
from pathlib import Path
import argparse
import numpy as np

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--label_directory', type=str, default="./labels",
                        help='path to folder with labels for annotation')
    parser.add_argument('--label_extention', type=str, default=".txt",
                        help='label extention - currently only for .txt')
    parser.add_argument('--img_directory', type=str, default="./images",
                        help='path to folder with images to be annotated')
    
    args = parser.parse_args()

    images = Path(args.img_directory)
    labels = Path(args.label_directory)


    for image in images.iterdir():
        
        img = cv2.imread(str(image))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)


        # Find contours, find rotated rectangle, obtain four verticies, and draw 
        cnts = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        rect = cv2.minAreaRect(cnts[0]) # ((CenterX, CenterY), (WidthX, WidthY), Angle)
        print(rect)
        box = np.int0(cv2.boxPoints(rect))
        print(box)
        cv2.drawContours(img, [box], 0, (36,255,12), 3) # OR
        # cv2.polylines(image, [box], True, (36,255,12), 3)

        cv2.imshow("result", img)
        cv2.waitKey(500)
        print(f"Frame: {image}")
    cv2.destroyAllWindows()
