import easyocr

reader = easyocr.Reader(['ch_sim'], gpu=True)
result = reader.readtext('chinese.jpg')

# import easyocr
# reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('chinese.jpg')

print(result)