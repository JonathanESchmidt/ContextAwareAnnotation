import argparse
from pathlib import Path
from random import randint


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_split', type=int, default="3", help='Choose number of categories for splitting')
    parser.add_argument('--img_directory', type=str, default="./images", help='path to folder with annotated images')
    parser.add_argument('--label_directory', type=str, default="./labels", help='path to folder with annotation labels')
    parser.add_argument('--train_directory', type=str, default="./train", help='path to folder for training images')
    parser.add_argument('--test_directory', type=str, default="./test", help='path to folder for test iamges')
    parser.add_argument('--val_directory', type=str, default="./validation", help='path to folder for validation')
    
    args = parser.parse_args()

    count = 0
    images = Path(args.img_directory)
    train_dir = Path(args.train_directory)
    test_dir = Path(args.test_directory)
    val_dir = Path(args.val_directory)
    label_dir = Path(args.label_directory)
    
    train_images_dir = train_dir / f"images"
    train_labels_dir = train_dir / f"labels"
    
    test_images_dir = test_dir / f"images"
    test_labels_dir = test_dir / f"labels"
    
    val_images_dir = val_dir / f"images"
    val_labels_dir = val_dir / f"labels"


    try:
        train_dir.mkdir(parents=False, exist_ok=False)
    except:
        pass
    
    try:
        test_dir.mkdir(parents=False, exist_ok=False)
    except:
        pass
    try:
        val_dir.mkdir(parents=False, exist_ok=False)
    except:
        pass
    try:
        train_images_dir.mkdir(parents=False, exist_ok=False)
    except:
        pass
    try:
        train_labels_dir.mkdir(parents=False, exist_ok=False)
    except:
        pass
    try:
        test_images_dir.mkdir(parents=False, exist_ok=False)
    except:
        pass
    try:
        test_labels_dir.mkdir(parents=False, exist_ok=False)
    except:
        pass

    try:
        val_images_dir.mkdir(parents=False, exist_ok=False)
    except:
        pass
    try:
        val_labels_dir.mkdir(parents=False, exist_ok=False)
    except:
        pass
    
    
    
    for image in images.iterdir():
        x = randint(1, 100)    # Pick a random number between 1 and 100.

        if x <= 70:
            dst = train_images_dir / image.name
            label_dst = train_labels_dir / f"{image.stem}.txt"
            

        elif x > 70 and x <= 80:
            dst = val_images_dir / image.name
            label_dst = val_labels_dir / f"{image.stem}.txt"

        else:
            dst = test_images_dir / image.name
            label_dst = test_labels_dir / f"{image.stem}.txt"

        label = Path(f"{label_dir}/{image.stem}.txt")
        label.rename(label_dst)
        image.rename(dst)