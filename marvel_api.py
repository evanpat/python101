import json
import requests
import time

ts = time.time()
#r = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
#r = requests.get("https://deckofcardsapi.com/api/dec   k/oo0tviree9s5/draw/?count=2")
#r = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=969478e7&t=hunger game")
#r = requests.get("https://api.adviceslip.com/advice")
r = requests.get(f"https://gateway.marvel.com/v1/public/characters?apikey=558b37f5b61da97b1872933a34b8a522&hash=klasjfkjkhlkjhk&ts={ts}")

c = r.content
cc = json.loads(c)
print(json.dumps(cc, indent=2))

#print(f'my login is {cc["login"]}')
