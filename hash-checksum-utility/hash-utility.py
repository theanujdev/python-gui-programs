import tkinter as tk
from tkinter import ttk
import pyperclip as cb


root = tk.Tk()
root.title('Hash Authentication Utility')
root.geometry("1470x650")
root.minsize(1070, 611)
root.configure(bg="white")

hash_value = tk.StringVar()

#-------------------Functions--------------------#


def reset():
    pass


def verify():
    pass


#---------Heading and statusbar-----------#
heading_label = tk.Label(root, text="Hash Authentication Utility",
                         font="Helvetica 30 bold", bg="white", fg='purple3')
heading_label.pack(pady=10, side=tk.TOP, fill=tk.X)
statusbar = tk.Label(root, text="STATUS BAR",
                     relief='sunken', anchor='w', padx=20, pady=5)
statusbar.pack(fill=tk.X, side=tk.BOTTOM)

#------------------Bottom Frame-------------------#
bottom_frame = tk.Frame(root, bg='white')

button_frame = tk.Frame(bottom_frame, bg='white')
verify_button = ttk.Button(button_frame, text='Verify', command=verify)
verify_button.pack(side=tk.LEFT, padx=20)
reset_button = ttk.Button(button_frame, text='Reset', command=reset)
reset_button.pack(side=tk.RIGHT, padx=20)
button_frame.pack(side=tk.BOTTOM, pady=(0, 20))

entry_label = tk.Label(bottom_frame, text='Enter your hash below :', bg='white',
                       fg='green', font='15')
entry_label.pack(side=tk.TOP)

hash_label = tk.Label(bottom_frame, text='Hash:', bg='white', font="Helvetica 15",
                      fg='red', anchor='e', pady=20)
hash_label.pack(padx=(60, 0), pady=0, fill=tk.X,
                side=tk.LEFT)
hash_entry = tk.Entry(bottom_frame, textvariable=hash_value, bg='snow',
                      font="Helvetica 10", justify=tk.CENTER,  relief='sunken')
hash_entry.pack(padx=20, pady=0, fill=tk.X, expand=1, side=tk.LEFT)
paste_button = ttk.Button(bottom_frame, text='Paste',
                          command=lambda: hash_value.set(cb.paste()))
paste_button.pack(padx=20, pady=0, side=tk.RIGHT)

bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=1)

#------------------LEFT FRAME-------------------#
left_frame = tk.Frame(root, bg='white')
for name in ['File:', 'MD5:', 'SHA-1:', 'SHA-256:', 'SHA-512:']:
    _ = tk.Label(left_frame, text=name, bg='white', font="Helvetica 15",
                 fg='purple3', anchor='e',  pady=18)
    _.pack(padx=20, pady=0, fill=tk.X)
left_frame.pack(side=tk.LEFT, fill=tk.X)

#------------------MID FRAME-------------------#
mid_frame = tk.Frame(root, bg='white')
browse_label = tk.Label(mid_frame, width=10, font="15", bg='ghost white',
                        padx=15, pady=2, relief='sunken')
browse_label.pack(pady=20, fill=tk.X)
md5_label = tk.Label(mid_frame, width=10, font="Arial 10", bg='ghost white',
                     padx=15, pady=2, relief='sunken')
md5_label.pack(pady=20, fill=tk.X)
sha1_label = tk.Label(mid_frame, width=10, font="Arial 10", bg='ghost white',
                      padx=15, pady=2, relief='sunken')
sha1_label.pack(pady=20, fill=tk.X)
sha256_label = tk.Label(mid_frame, width=10, font="Arial 10", bg='ghost white',
                        padx=15, pady=2, relief='sunken')
sha256_label.pack(pady=20, fill=tk.X)
sha512_label = tk.Label(mid_frame, font="Arial 10", bg='ghost white',
                        padx=15, pady=2, relief='sunken')
sha512_label.pack(pady=20, fill=tk.X)
mid_frame.pack(side=tk.LEFT, fill=tk.X, expand=1)

root.mainloop()
