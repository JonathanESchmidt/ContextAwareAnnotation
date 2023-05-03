import numpy as np
import argparse
from pathlib import Path
import cv2


def saveDetection(ID, x, y, width, height, filename):
    with open(filename, 'a+', newline='') as file:
        file.write(f'{ID},{x},{y},{width},{height}')
        file.write('\n')


def centerStyle(class_ID, x, y, width, height, label):
    x_center = x + width/2
    y_center = y + height/2
    saveDetection(class_ID, x_center, y_center, width, height, label)


def cornersStyle(class_ID, x, y, width, height, label):
    x1 = x
    y1 = y
    x2 = x + width
    y2 = y + height
    saveDetection(class_ID, x1, y1, x2, y2, label)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--BBtype', type=str, default="center",
                        help='Type of annotation. Choose: center, corner or corners')
    parser.add_argument('--class_ID', type=int, default=0,
                        help='saved class ID for annotation')
    parser.add_argument('--img_directory', type=str, default="./images",
                        help='path to folder with images to be annotated')
    parser.add_argument('--label_directory', type=str, default="./labels",
                        help='path to folder with labels for annotation')
    parser.add_argument('--label_extention', type=str, default=".txt",
                        help='label extention - currently only for .txt')
    parser.add_argument('--combine_BB', type=bool, default="False",
                        help='combine BBoxes for certain types of annotation.')

    args = parser.parse_args()

    labels = Path(args.label_directory)

    try:
        labels.mkdir(parents=False, exist_ok=False)
    except:
        pass

    images = Path(args.img_directory)
    for image in images.iterdir():

        img = cv2.imread(str(image))
        label = labels / f"{image.stem}{args.label_extention}"

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(
            binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if not args.combine_BB:
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)

                if args.BBtype == "center":
                    centerStyle(args.class_ID, x/img.shape[1], y/img.shape[0],
                                w/img.shape[1], h/img.shape[0], label)
                elif args.BBtype == "corners":
                    cornersStyle(args.class_ID, x/img.shape[1], y/img.shape[0],
                                w/img.shape[1], h/img.shape[0], label)

                elif args.BBtype == "corner":
                    saveDetection(args.class_ID, x/img.shape[1], y/img.shape[0],
                                w/img.shape[1], h/img.shape[0], label)
        
        elif args.combine_BB:
            x_min = 99999
            x_max = -1
            y_min = 99999
            y_max = -1

            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)

                if x < x_min: x_min = x
                if x + w > x_max: x_max = x + w
                if y < y_min: y_min = y
                if y + h > y_max: y_max = y + h

            if args.BBtype == "center":
                centerStyle(args.class_ID, x_min/img.shape[1], y_min/img.shape[0],
                                (x_max - x_min)/img.shape[1], (y_max - y_min)/img.shape[0], label)
            elif args.BBtype == "corners":
                cornersStyle(args.class_ID, x_min/img.shape[1], y_min/img.shape[0],
                                (x_max - x_min)/img.shape[1], (y_max - y_min)/img.shape[0], label)

            elif args.BBtype == "corner":
                saveDetection(args.class_ID, x_min/img.shape[1], y_min/img.shape[0],
                                (x_max - x_min)/img.shape[1], (y_max - y_min)/img.shape[0], label)