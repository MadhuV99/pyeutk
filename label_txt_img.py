# label_txt_img.py
import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="python_logo_small.gif")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

# Text cntered on top of image
# w = tk.Label(root, 
#              compound = tk.CENTER,
#              text=explanation, 
#              image=logo).pack(side="right")

# image on the right side and the text left justified with a padding of 10 pixels on both sides
w = tk.Label(root, 
          justify=tk.LEFT,
          compound = tk.RIGHT,
          padx = 10, 
          text=explanation, 
          image=logo).pack()

root.mainloop()
