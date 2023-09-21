from PIL import Image
with Image.open("images/800px-MPSS_Mario.webp") as im:
    im.rotate(90).show()
