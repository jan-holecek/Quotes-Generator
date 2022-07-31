from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageOps
import random
import api
from algoritmus import SortMessage
from algoritmus import * 

quote_text = api.content

#black 
MAX_W, MAX_H = 1080, 1080
img = Image.open('img/background_black.png')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('fonts/Playfair-font.ttf', 90)

text = SortMessage(quote_text, 20)
bounding_box = [0, 0, MAX_W-1, MAX_H-1]
x1, y1, x2, y2 = bounding_box
w, h = draw.textsize(text, font=font)
x = (x2 - x1 - w)/2 + x1
y = (y2 - y1 - h)/2 + y1

draw.text((x, y), text, font = font, fill = "white", align="center")

number = random.randint(0, 150)

img.save("img/black/citat_cerny" + str(number) + ".png", 'PNG')
print(f"Citát ČERNÝ byl úspešně vygenerován. (číslo: {str(number)})")


#white
img2 = Image.open('img/background_white.png')
draw2 = ImageDraw.Draw(img2)

draw2.text((x, y), text, font = font, fill = "black", align="center")

img2.save("img/white/citat_bily" + str(number) + ".png", 'PNG')
print(f"Citát BÍLÝ byl úspešně vygenerován. (číslo: {str(number)})")
