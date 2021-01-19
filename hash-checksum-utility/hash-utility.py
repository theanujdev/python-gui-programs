import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Hash Authentication Utility')
root.geometry("1470x650")
root.minsize(1070, 611)
root.configure(bg="white")

#---------Heading and statusbar-----------#
heading_label = tk.Label(root, text="Hash Authentication Utility",
                         font="Helvetica 30 bold", bg="white", fg='purple3')
heading_label.pack(pady=10, side=tk.TOP, fill=tk.X)
statusbar = tk.Label(root, text="STATUS BAR",
                     relief='sunken', anchor='w', padx=20, pady=5)
statusbar.pack(fill=tk.X, side=tk.BOTTOM)

root.mainloop()
