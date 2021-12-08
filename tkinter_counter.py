import tkinter as tk

def increase():
  c = int(number['text'])
  c = c + 1
  number['text'] = c

window = tk.Tk()
window.title("Counter")

btn1 = tk.Button(text="-", width=5, height=5)
btn1.grid(row=0, column=0)

number = tk.Label(text='0')
number.grid(row=0, column=1, padx=10)

btn2 = tk.Button(text="+", width=5, height=5, command=increase)
btn2.grid(row=0, column=2)

tk.mainloop()
