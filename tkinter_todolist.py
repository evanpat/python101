import tkinter as tk
import tkinter.messagebox as mesgbox
import pickle

window = tk.Tk()
window.title("To Do List")
window.resizable(False, False)

def add_task():
  task = entry.get()
  if len(task) > 0:
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)
  else:
    mesgbox.showwarning(title="Warning!", message="You must enter a task")

def delete_task():
  if len(listbox.curselection()) > 0:
    index = listbox.curselection()[0]
    listbox.delete(index)
  else:
    mesgbox.showwarning(title="Warning!", message="Please select a task")

def load_task():
    listbox.delete(0, tk.END)
    tasks = pickle.load(open("save.dat", "rb"))
    for task in tasks:
      listbox.insert(tk.END, task)


def save_task():
  tasks = listbox.get(0, listbox.size())
  pickle.dump(tasks, open("save.dat", "wb"))

frame = tk.Frame(window)
frame.pack()

listbox = tk.Listbox(frame, height=10, width=50)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill='y')
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(window, width=50)
entry.pack(fill='x', expand=True)
entry.focus()

add_button = tk.Button(window, text="Add Task", width=25, command=add_task)
add_button.grid(row=0, column=0, sticky="s")
# add_button.pack(fill='x', expand=True)

del_button = tk.Button(window, text="Delete Task", width=25, command=delete_task)
del_button.grid(row=0, column=1, sticky="s")
# del_button.pack(fill='x', expand=True)

load_button = tk.Button(window, text="Load Tasks", width=25, command=load_task)
load_button.grid(row=1, column=0, sticky="s")
# load_button.pack(fill='x', expand=True)

save_button = tk.Button(window, text="Save Tasks", width=25, command=save_task)
save_button.grid(row=1, column=0, sticky="s")
# save_button.pack(fill='x', expand=True)

tk.mainloop()