import sys
import os
from PIL import Image, ImageFilter

# grab first and second argument
jpeg_folder = sys.argv[1]
png_folder = sys.argv[2]

# check if new(png) folder exists, if not create it
if not os.path.exists(png_folder):
    try:
        os.mkdir(png_folder)
    except OSError:
        print(f"Creation of the folder {png_folder} failed")
    else:
        print(f"Successfully created the folder {png_folder}")

# loop through Pokedex ,
for filename in os.listdir(jpeg_folder):
    if (filename.endswith(".jpg")):
        jpg_img = Image.open(f"{jpeg_folder}/{filename}")
        new_img_name = os.path.splitext(filename)[0]
        # convert images to png
        # save to the new folder
        jpg_img.save(f"{png_folder}/{new_img_name}.png", "png")
