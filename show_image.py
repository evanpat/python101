from PIL import Image

#pic = "images/800px-MPSS_Mario.webp"
pic = "images/cartoon.jpg"
pic1 = "images/cartoon1.png"
pic2 = "images/cartoon2.png"

with Image.open(pic) as im:
    print(pic, im.format, f"{im.size}x{im.mode}")
    im1 = im.convert('L').point(lambda i: i * 2)
    im1.save(pic1, "PNG")

    left = 0
    top = 0
    h = 180 
    w = 180 
    im2 = im.crop((left, top, h, w))
    im2.save(pic2)

#Image.open(pic2).show()
