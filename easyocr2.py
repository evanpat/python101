import easyocr
from googletrans import Translator


reader = easyocr.Reader(['ar'], gpu=True)
result = reader.readtext('images/arabic.jpg', detail=0)

str = ""
for r in result:
    str += r

print(str)

translator = Translator()
translations = translator.translate(str, dest="en")

for translation in translations:
     print(translation.origin, ' -> ', translation.text)