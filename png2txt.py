from PIL import Image

import pytesseract

t = 'test'
output= f'{t}.txt' #where you want to save and file name
f=open(output, "a")

idx= f"{t}.png"         
text=str(pytesseract.image_to_string(Image.open(idx)))
f.write(text)
f.close()