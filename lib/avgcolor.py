from PIL import Image
def get_avg_color(img):
    pixels = list(img.getdata())

    divisor = 0
    r = 0
    g = 0
    b = 0

    for i in pixels:
        if (i != (255, 255, 255)):
            divisor += 1
            r += i[0]
            g += i[1]
            b += i[2]

    #size = img.width * img.height
    avg_r = int(r / divisor)
    avg_g = int(g / divisor)
    avg_b = int(b / divisor)

    return (avg_r, avg_g, avg_b)