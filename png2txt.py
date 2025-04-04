from PIL import Image

import pytesseract

fname = 'test'

input_png = f"{fname}.png"       
try:  
    text = str(pytesseract.image_to_string(Image.open(input_png)))

    output_txt = f'{fname}.txt' #where you want to save and file name
    fw = open(output_txt, "a")

    fw.write(text)
    fw.close()
except: 
    print("Some error")