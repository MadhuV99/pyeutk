# label_text.py
import tkinter as tk

root = tk.Tk()
tk.Label(root, 
         text="Red Text in Times Font, default background",
         fg = "red",
         font = "Times").pack()
tk.Label(root, 
         text="Light Green Text in Helvetica Font, dark green background",
         fg = "light green",
         bg = "dark green",
         font = "Helvetica 16 bold italic").pack()
tk.Label(root, 
         text="Blue Text in Verdana bold, yellow background",
         fg = "blue",
         bg = "yellow",
         # font = "Verdana 10 bold"
         font = ("Times New Roman", 10, "bold italic")
         ).pack()

root.mainloop()
