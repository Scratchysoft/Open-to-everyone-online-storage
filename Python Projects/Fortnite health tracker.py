import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string

# Path of working folder on Disk
src_path = "tes-img/"

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    # Remove template file
    #os.remove(temp)

    return result


print('--- Start recognize text from image ---')
print(get_string(img) )

print("------ Done -------")
