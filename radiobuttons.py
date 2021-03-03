# radiobuttons.py
import tkinter as tk

root = tk.Tk()

v = tk.IntVar()

def write_choice():
    print('You chose:', v.get())

tk.Label(root, 
        text="""Choose a 
programming language:""",
        justify = tk.LEFT,
        padx = 20).pack()

tk.Radiobutton(root, 
               text="Python",
               padx = 20, 
               variable=v,
               value=1).pack(anchor=tk.W)
tk.Radiobutton(root, 
               text="Perl",
               padx = 20, 
               variable=v, 
               value=2).pack(anchor=tk.W)
v.set(2)
choice = tk.Button(root,
                   text="Hello",
                   command=write_choice).pack()

root.mainloop()