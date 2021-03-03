# messages.py
import tkinter as tk
root = tk.Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(root, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()

btn = tk.Button(root, text="Quit", width=8, command=root.quit)
btn.pack(pady=10)

tk.mainloop()
