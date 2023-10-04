import easyocr

reader = easyocr.Reader(['ch_sim'], gpu=True)
result = reader.readtext('chinese.jpg', detail=0)

str = ""
for r in result:
    str += r

print(str)