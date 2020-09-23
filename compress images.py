# install Pillow with pip install pillow
import PIL
from PIL import Image
from tkinter.filedialog import *

# Ask users the location of the image file in their directory
file_path = askopenfilename()
img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth) , PIL.Image.ANTIALIAS)

# save as jpg
save_path = asksaveasfilename()

img.save(save_path+"_compressed.JPG")