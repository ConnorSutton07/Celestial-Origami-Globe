from PIL import Image

def concat_img(im1, im2a, im2b, f_triangles, im4, b_triangles, im6, color=(255, 255, 255)):
    new_img = Image.new('RGB', (im1.width * 4, im1.height * 4), color)
    new_img.paste(im1, (int(im1.width * 1.5), int(im1.height * 1.5)))
    new_img.paste(im2a, (int(im1.width * 3.5), int(im1.height * 1.5)))
    new_img.paste(im2b, (0, int(im1.height * 1.5)))
    new_img.paste(im4, (int(im1.width * 2.5), int(im1.height * 1.5)))
    new_img.paste(im6, (int(im1.width * 0.5), int(im1.height * 1.5)))
    new_img.paste(b_triangles[3], (int(im1.width * 0.5), int(im1.height * 0.5)))
    new_img.paste(b_triangles[2], (int(im1.width * 1.5), int(im1.height * 0.5)))
    new_img.paste(b_triangles[1], (int(im1.width * 2.5), int(im1.height * 0.5)))
    new_img.paste(f_triangles[3], (int(im1.width * 0.5), int(im1.height * 2.5)))
    new_img.paste(f_triangles[0], (int(im1.width * 1.5), int(im1.height * 2.5)))
    new_img.paste(f_triangles[1], (int(im1.width * 2.5), int(im1.height * 2.5)))

    tr = b_triangles[0].crop((0, 0, b_triangles[0].width / 2, b_triangles[0].height))
    tl = b_triangles[0].crop((b_triangles[0].width / 2, 0, b_triangles[0].width, b_triangles[0].height))
    br = f_triangles[2].crop((0, 0, f_triangles[2].width / 2, f_triangles[2].height))
    bl = f_triangles[2].crop((f_triangles[2].width / 2, 0, f_triangles[2].width, f_triangles[2].height))

    new_img.paste(tr, (int(im1.width * 3.5), int(im1.height * 0.5)))
    new_img.paste(tl, (0, int(im1.height * 0.5)))
    new_img.paste(br, (int(im1.width * 3.5), int(im1.height * 2.5)))
    new_img.paste(bl, (0, int(im1.height * 2.5)))
    
    return new_img 