import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import hashlib
import pyperclip as cb

root = tk.Tk()
root.title('Hash Authentication Utility')
root.geometry("1470x650")
root.minsize(1070, 611)
root.configure(bg="white")

hash_value = tk.StringVar()

#-------------------Functions--------------------#


def ask_file():
    file = filedialog.askopenfilename(title="Folder")
    if file:
        browse_label['text'] = file
        statusbar['text'] = 'File : ' + file
        set_hash(file)


def set_hash(file):
    try:
        hash_md5 = hashlib.md5()
        hash_sha1 = hashlib.sha1()
        hash_sha256 = hashlib.sha256()
        hash_sha512 = hashlib.sha512()
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(1024), b""):  # 4096 or 1024 bytes
                hash_md5.update(chunk)
                hash_sha1.update(chunk)
                hash_sha256.update(chunk)
                hash_sha512.update(chunk)

        md5_label['text'] = hash_md5.hexdigest()
        sha1_label['text'] = hash_sha1.hexdigest()
        sha256_label['text'] = hash_sha256.hexdigest()
        sha512_label['text'] = hash_sha512.hexdigest()

    except Exception as e:
        statusbar['text'] = "Error : " + str(e)


def reset():
    browse_label['text'] = ''
    md5_label['text'] = ''
    sha1_label['text'] = ''
    sha256_label['text'] = ''
    sha512_label['text'] = ''
    hash_entry.delete(0, tk.END)
    statusbar['bg'] = 'SystemButtonFace'
    statusbar['text'] = "STATUS BAR"


def verify():
    pure_hash = hash_value.get().strip()
    hash_value.set(pure_hash)
    hashes = {'MD5': md5_label['text'],
              'SHA-1': sha1_label['text'],
              'SHA-256': sha256_label['text'],
              'SHA-512': sha512_label['text']}
    for name, value in hashes.items():
        if pure_hash == value:
            statusbar['text'] = 'Matching hash : ' + name
            statusbar['bg'] = 'OliveDrab1'
            messagebox.showinfo(
                "Info", name + " hash matched!\nFile is original.")
            return
    statusbar['text'] = "No hash matched. File is not original !"
    statusbar['bg'] = 'tan1'
    messagebox.showwarning("Info", "No hash matched.\nFile is not original!")


#-------------------Heading and statusbar-----------------------#
heading_label = tk.Label(root, text="Hash Authentication Utility",
                         font="Helvetica 30 bold", bg="white", fg='purple3')
heading_label.pack(pady=10, side=tk.TOP, fill=tk.X)
statusbar = tk.Label(root, text="STATUS BAR",
                     relief='sunken', anchor='w', padx=20, pady=5)
statusbar.pack(fill=tk.X, side=tk.BOTTOM)

#-----------------------Bottom Frame---------------------------#
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

#--------------------------LEFT FRAME-------------------------#
left_frame = tk.Frame(root, bg='white')
for name in ['File:', 'MD5:', 'SHA-1:', 'SHA-256:', 'SHA-512:']:
    _ = tk.Label(left_frame, text=name, bg='white', font="Helvetica 15",
                 fg='purple3', anchor='e',  pady=18)
    _.pack(padx=20, pady=0, fill=tk.X)
left_frame.pack(side=tk.LEFT, fill=tk.X)

#-------------------------RIGHT FRAME-------------------------#
right_frame = tk.Frame(root, bg='white')
browse_button = ttk.Button(right_frame, text='Browse',
                           command=ask_file)
browse_button.pack(pady=19)
md5_button = ttk.Button(right_frame, text='Copy MD5',
                        command=lambda: cb.copy(md5_label['text']))
md5_button.pack(pady=19)
sha1_button = ttk.Button(right_frame, text='Copy SHA-1',
                         command=lambda: cb.copy(sha1_label['text']))
sha1_button.pack(pady=19)
sha256_button = ttk.Button(right_frame, text='Copy SHA-256',
                           command=lambda: cb.copy(sha256_label['text']))
sha256_button.pack(pady=19)
sha512_button = ttk.Button(right_frame, text='Copy SHA-512',
                           command=lambda: cb.copy(sha512_label['text']))
sha512_button.pack(pady=19)
right_frame.pack(padx=20, side=tk.RIGHT)

#---------------------------MID FRAME--------------------------#
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
