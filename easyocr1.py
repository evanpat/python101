import easyocr

reader = easyocr.Reader(['ch_sim', 'en'], gpu=True)
result = reader.readtext('images/code.png', detail=1)

# str = ""
# for r in result:
#     str += r

print(result)

#cpu - computer processing unit (Intel i5, i7, AMD)
#gpu - graphics processing unit (Nvidia)

# confidence level