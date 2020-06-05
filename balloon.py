import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
from lib.avgcolor import get_avg_color
from lib.concat import concat_img
import lib.draw as ld
from mpl_toolkits.basemap import Basemap
from PIL import Image, ImageDraw

n_colors = 0
line_angle = 36
width = 0.95e7
height = 0.94e7
using_image = input("Would you like to use an image? (y/n): ")
im_file = ''

if (using_image == 'y'):
    im_file = input("Enter image file: ")
    if (im_file[-4] != "."):
       im_file += ".png"

    try:
        im = Image.open(im_file)
    except:
        print("Image could not be found. ")
        exit()

    im_width = im.width
    im_height = im.height

    #warpimage will not work when an image's width is larger than twice the height, so it will need to be resized
    if (im_width > (im_height * 2)):
        print("Image width larger than twice the height, resizing to 2:1 ratio")
        im = im.resize((im_height * 2, im_width))
        
    #quantizes image
    n_colors = input("How many colors? (or say all) ")
    try:
        n_colors = int(n_colors)
        im = im.quantize(int(n_colors))
        im.save('quantized_img.png', "PNG")
    except:
        im.save('quantized_img.png', "PNG")

    

#the lon/lat coordinates and temporary file names of the center of the north pole, south pole, front, right, back, and left faces respectively
coords = [(0, 90), (0, -90), (0, 0), (90, 0), (180, 0), (270, 0)]
file_names = ["north_pole.png", "south_pole.png", "front_face.png", "right_face.png", "back_face.png", "left_face.png"]

#creates the 6 squares
for i in range (0, 6):
    m = Basemap(projection = "aeqd", lat_0 = coords[i][1], lon_0 = coords[i][0], width = width, height = height)
    if (using_image != 'y'):
        m.drawmapboundary(fill_color = "aqua")
        m.drawcoastlines(linewidth = 0.5)
        m.fillcontinents(color = "coral", lake_color = "aqua")
    else:
        m.warpimage("quantized_img.png")

    m.drawparallels(np.arange(-90, 90, line_angle))
    m.drawmeridians(np.arange(-180, 180, line_angle))

    plt.axis('off')
    plt.savefig(file_names[i], bbox_inches = "tight", pad_inches = 0)
    plt.clf()


img1 = Image.open('north_pole.png')
img2 = Image.open('south_pole.png').rotate(180)

f_triangles = []
b_triangles = []
for i in range(0, 4):
    f_triangles.insert(i, Image.open('front_face.png'))
    b_triangles.insert(i, Image.open('back_face.png'))
    b_triangles[i] = b_triangles[i].rotate(180)

img4 = Image.open('right_face.png').rotate(90)
img6 = Image.open('left_face.png').rotate(270)

#split south pole into 2 images
sp_width, sp_height = img2.size
sp1 = img2.crop((0, 0, sp_width / 2, sp_height))
sp2 = img2.crop((sp_width / 2, 0, sp_width, sp_height))

#split the front and back squares into 4 triangles each
f_triangles[0] = ld.draw_triangles(f_triangles[0], False, True, True, True)
f_triangles[1] = ld.draw_triangles(f_triangles[1], True, False, True, True).rotate(90)
f_triangles[2] = ld.draw_triangles(f_triangles[2], True, True, False, True).rotate(180)
f_triangles[3] = ld.draw_triangles(f_triangles[3], True, True, True, False).rotate(270)

b_triangles[0] = ld.draw_triangles(b_triangles[0], False, True, True, True).rotate(180)
b_triangles[1] = ld.draw_triangles(b_triangles[1], True, False, True, True).rotate(270)
b_triangles[2] = ld.draw_triangles(b_triangles[2], True, True, False, True)
b_triangles[3] = ld.draw_triangles(b_triangles[3], True, True, True, False).rotate(90)

#stores concantenated image in variable final_img
final_img = concat_img(img1, sp1, sp2, f_triangles, img4, b_triangles, img6)

#gets the avg_color of the image to use for drawing
avg_color = get_avg_color(final_img)

#remove weird black lines from the triangles
final_img = ld.draw_white_lines(final_img)

# draw black lines along borders
final_img = ld.draw_black_lines(final_img)

#draws all the shapes and dashes
final_img = ld.draw_shapes(final_img, avg_color)

new_file_name = input("What would you like to name the new image? ")

#makes sure the file has valid name
if (new_file_name[-4:] != ".png"):
    new_file_name += ".png"


#saves and shows final image
final_img.save(new_file_name, "PNG")
final_img.show()

#remove temporary img files
os.remove('north_pole.png')
os.remove('south_pole.png')
os.remove('front_face.png')
os.remove('right_face.png')
os.remove('back_face.png')
os.remove('left_face.png')
if (using_image == 'y'):
    os.remove('quantized_img.png')


