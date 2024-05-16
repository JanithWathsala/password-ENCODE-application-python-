import tkinter as tk
from tkinter import ttk
import base64

root = tk.Tk()
root.geometry("400x200")
root.title("Encode password")

ent_pwd = ttk.Label(root, text="Enter your password", font=("arial", 10, "bold"))
ent_pwd.pack()

frame = ttk.Frame(root, width=400, height=60)
frame.pack()

task_entry = ttk.Entry(frame, font="arial 18", width=27)
task_entry.pack()


encode_button = ttk.Button(root, text="Encode")
encode_button.pack(pady=5)

encode_num = ttk.Label(root, text="", font=("arial", 10))
encode_num.pack()

root.mainloop()
 

