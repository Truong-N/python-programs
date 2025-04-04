from PIL import Image

import pytesseract

fname = 'test'
output_txt = f'{fname}.txt' #where you want to save and file name
fw = open(output_txt, "a")

input_png = f"{fname}.png"         
text = str(pytesseract.image_to_string(Image.open(input_png)))
fw.write(text)
fw.close()