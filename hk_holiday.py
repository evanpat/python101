import json
import requests

#r = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
#r = requests.get("https://deckofcardsapi.com/api/dec   k/oo0tviree9s5/draw/?count=2")
#r = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=969478e7&t=hunger game")
#r = requests.get("https://api.adviceslip.com/advice")
#r = requests.get("https://api.funtranslations.com/translate/emoji.json?text=Apple%20is%20great%20fruit%20fries%20are%20yummy%20when%20you%20are%20in%20the%20car")

r = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/hello")



c = r.content
cc = json.loads(c)
print(json.dumps(cc, indent=2))

print(f'{cc[0]["meanings"][0]["definitions"][0]["definition"]}')

