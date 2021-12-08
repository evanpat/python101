import tkinter as tk
def convert():
    f = entry.get()
    if f.isnumeric():
      c = (5/9) * (float(f) - 32)
      lbl_result["text"] = f"{round(c, 2)} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Converter")
# must have weight for resize to work
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=100, weight=1)
#window.resizable(width=False, height=False)


frame = tk.Frame(master=window)

entry = tk.Entry(master=frame, width=10)
entry.grid(row=0, column=0, sticky="ew")

f_label = tk.Label(master=frame, text="\N{DEGREE FAHRENHEIT}")
f_label.grid(row=0, column=1, sticky="ew")

button = tk.Button(
    master=window,
    text="-->",
    command=convert
)

lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frame.grid(row=0, column=0, padx=10, sticky="w")
button.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10, sticky="e")

window.mainloop()
