#!/usr/bin/python3

# ^^ just in case I ever run this from command line

from PIL import Image

img = Image.open('pineapple.jpeg','r')

pix_val = list(img.getdata())
input("done")
#print(pix_val)

not_white = []
summ = 0
for pixel in pix_val:
    summ = 0
    for num in pixel:
        summ += num
    if summ != 765:
        not_white.append(pixel)

print(not_white)