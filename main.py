import tkinter as tk
from tkinter import ttk
import base64
import pyperclip

def add_task(event=None):
    password = task_entry.get()
    encode_password = base64.b64encode(password.encode()).decode()
    encode_num.config(text=f"Encode password:{encode_password}")
    
def copy_encode():
    password = task_entry.get()
    encode_password = base64.b64encode(password.encode()).decode()
    pyperclip.copy(encode_password)

root = tk.Tk()
root.geometry("400x200")
root.title("Encode password")

ent_pwd = ttk.Label(root, text="Enter your password", font=("arial", 10, "bold"))
ent_pwd.pack()

frame = ttk.Frame(root, width=400, height=60)
frame.pack()

task_entry = ttk.Entry(frame, font="arial 18", width=27)
task_entry.pack()

task_entry.bind("<Return>", add_task)

encode_button = ttk.Button(root, text="Encode", command=add_task)
encode_button.pack(pady=5)

encode_num = ttk.Label(root, text="", font=("arial", 10))
encode_num.pack()

copy_button = ttk.Button(root, text="Copy to encode")
copy_button.pack(pady=5)

root.mainloop()
 

