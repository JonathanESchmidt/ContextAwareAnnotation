import cv2
from pathlib import Path
import argparse

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


        content = Path(labels / f"{image.stem}{args.label_extention}").read_text(encoding="utf-8")
        boxes = [line for line in content.splitlines()]
        # print("\n".join(boxes))

        for box in boxes:
            boxVals = box.split(",")
            width = int(float(boxVals[3])*img.shape[0])
            height = int(float(boxVals[4])*img.shape[1])
            x = int(float(boxVals[1])*img.shape[0] - width/2)
            y = int(float(boxVals[2])*img.shape[1] - height/2)

            cv2.rectangle(img, (x, y), (x+width, y+height), (255, 0, 0), 3)
        cv2.imshow("result", img)
        cv2.waitKey(5)
        print(f"Frame: {image}")
    cv2.destroyAllWindows()
