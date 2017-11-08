#!/usr/bin/python3
# ^^ just in case I ever run this from command line


#imports
from PIL import Image

#open image file
img = Image.open('pineapple.jpeg','r')

#get pixel metadata
pix_val = list(img.getdata())
input("done")
#print(pix_val)      #<-- massive print statement 

#add all pixels that aren't white to a new list
not_white = []
summ = 0
for pixel in pix_val:
    summ = 0
    for num in pixel:
        summ += num
    if summ != 765:
        not_white.append(pixel)
print(not_white)