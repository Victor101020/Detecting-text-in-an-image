import pytesseract
from PIL import Image


img = Image.open(r'E:\\pyrhon\\progectTEST\\Detecting text in an image\\Image Labrary\\2.jpg')

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

config_custom = r'--oem 3 --psm 13'

text = pytesseract.image_to_string(img, lang='rus')
print(text)