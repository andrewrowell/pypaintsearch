from PIL import Image
import pytesseract
print(pytesseract.image_to_boxes(Image.open("images/source/20200526_122643.jpg")))
