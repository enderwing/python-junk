# Import Moduels
from time import sleep
import random

# Check if we are importaing from an existing save
# if input("Type `i` to import from a file, or type `n` for a new game") == "i":
# 	load_file = open(input("what is the path to your save file"), 'r')
# print(load_file.readline())
load_file = open("./output_file", 'r+')
print(load_file.readline(), end='')
print(load_file.readline(), end='')