import tkinter as tk

window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")


# label
hello = tk.Label(text="Hello world!", fg='white', bg='black')
hello.pack()

# button
button = tk.Button(text="Click me!")
button.pack()

# entry
ent = tk.Entry()
ent.pack()

# text (multi-line)
txt = tk.Text()
txt.pack()

tk.mainloop()
