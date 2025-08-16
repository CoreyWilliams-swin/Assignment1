#preprocessor.py
#install script for libs
#py -m pip install --upgrade pip
#py -m pip install pillow numpy

import argparse
from pathlib import Path
import csv 
import numpy as np
from PIL import Image

def prepare(input_path):
    p = Path(input_path)
    img = Image.open(p)
    print("Image loaded.")
    category = p.stem[0] if p.stem else ""
    out_img_path = p.with_name(f"{p.stem}_preprocessed.png")
    csv_path = p.parent / "IMAGES_PREPROCESSED.csv"
    print("Prepared.")
    return img, category, out_img_path, csv_path


def grayscale(img):
    return img

def invert(img):
    return img

def crop(img):
    return img

def resize(img):
    return img

def pad_image(img):
    return img

def deskew(img):
    return img

def center(img):
    return img



def convert_csv(csv_path, img, label):
    
    img_csv = img.convert("L") #needed for testing
    if img_csv.size != (28, 28): #same
        img_csv = img_csv.resize((28, 28))  #same
    pixels = list(img_csv.getdata())       

    with open(csv_path, "a", newline="") as f:
        w = csv.writer(f)

        w.writerow([label] + pixels)


def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("input") 
        args = parser.parse_args()
        img_path = Path(args.input)

        img, category, out_img_path, csv_path = prepare(img_path)
      
        print("Begun preprocessing...")

        img = grayscale(img)
        img = invert(img)
        img = crop(img)
        img = resize(img)
        img = pad_image(img)
        img = deskew(img)
        img = center(img)

        print("Ended Preprocessing...")
     

        out_img_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(out_img_path)
        print("Image saved")
     
        label = int(category) if str(category).isdigit() else -1
        convert_csv(csv_path, img, label)
        print("Converted to CSV")

        return img 

if __name__ == "__main__":
    main()