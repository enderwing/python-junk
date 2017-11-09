#!/usr/bin/python3
# ^^ just in case I ever run this from command line

'''Eventually this file may do something slghtly more useful (probably not) but for now:
    Asks user for a file path and the file extension separately (parsing is 'hard' and it's late)
    Makes a "condensed" version of the image. A version with all white pixels removed and squished
    to the top left. Then makes an image that is the original image but all of the pixels are 
    placed in a random order.
'''
    


#imports
from PIL import Image
import random

#open image file
img_file_path = input("image path (from current directory, exclude file extension)\n>>> ")
img_file_ext = input("File extnsion of the image (png, jpeg, etc.\n>>> ")
img = Image.open(img_file_path+'.'+img_file_ext,'r')

#get pixel metadata
pix_val = list(img.getdata())
input("done")
#print(pix_val)                 #<-- massive print statement 

#add all pixels that aren't white to a new list
not_white = []
summ = 0
for pixel in pix_val:
    summ = 0
    for num in pixel:
        summ += num
    if summ != 765:
        not_white.append(pixel)
#print(not_white)                #<-- takes ages to print

new_img = Image.new(img.mode, img.size)
new_img.putdata(not_white)
new_img.save('image_output1.' + img_file_ext)

rand_pix = pix_val
random.shuffle(rand_pix)
new_img = Image.new(img.mode, img.size)
new_img.putdata(rand_pix)
new_img.save('image_output2.' + img_file_ext)
