import pyautogui
import pytesseract
import cv2
import numpy
import PIL

'''
simple script to print out the text on screen of the selected coordinates on screen
'''

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

def tesser_image(image):
    # makes it twice as big so it is easier to read
    image = cv2.resize(image, (0,0), fx=2, fy=2)
    ret,image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    image = PIL.Image.fromarray(image, 'RGB')
    txt = pytesseract.image_to_string(image)
    return(txt)


def screengrab_as_numpy_array(location):
    """ ouputs the location as a tuple """
    im = numpy.array(PIL.ImageGrab.grab(bbox = (location[0], location[1], location[2], location[3])))
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    return(im)
# x,y coordinates for location on screen that you want to print out to console
print(tesser_image(screengrab_as_numpy_array((810, 300, 1130, 425))))
