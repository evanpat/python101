import tkinter as tk
import json
import requests
import vlc


def search():
  word = entry.get()
  r = requests.get(
    f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}",
    headers = {"Accept": "application/json"},
  )

  c = r.content
  cc = json.loads(c)

  data = json.dumps(cc, indent=2)
  text.insert(tk.INSERT, data)

  p = vlc.MediaPlayer("http://ssl.gstatic.com/dictionary/static/sounds/20200429/girl--_gb_1.mp3")
  p.play()



window = tk.Tk()
window.title("Dictionary")
window.resizable(False, False)


text = tk.Text(width=50)
text.pack()

entry = tk.Entry(width=52)
entry.pack()

add_button = tk.Button(text="Search", width=21, command=search)
add_button.pack()


tk.mainloop()