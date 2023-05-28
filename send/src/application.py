import tkinter as tk
import subprocess

def run_program():
    email = entry.get()
    subprocess.call(['send/src/check.py', email])

def stop_program():
    root.destroy()

root = tk.Tk()

label = tk.Label(root, text="E-Mail-Adresse:")
label.pack()

entry = tk.Entry(root)
entry.pack()

run_button = tk.Button(root, text="Run", command=run_program)
run_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_program)
stop_button.pack()

root.mainloop()




