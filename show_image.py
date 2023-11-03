from PIL import Image

with Image.open("images/800px-MPSS_Mario.webp") as im:
    black_and_white = im.convert("L")
    black_and_white.show()
    
    rotated_image = im.rotate(180)
    rotated_image.save("images/result.webp")
    


