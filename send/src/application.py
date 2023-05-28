import tkinter as tk
import subprocess

email = ""

def run_program():
    global email
    email_value = entry.get()
    email = email_value
    print("Email:", email)
    subprocess.call(['/usr/bin/python3', 'send/src/check.py'])

root = tk.Tk()

label = tk.Label(root, text="E-Mail-Adresse:")
label.pack()

entry = tk.Entry(root)
entry.pack()

run_button = tk.Button(root, text="Run", command=run_program)
run_button.pack()

if __name__ == "__main__":
    root.mainloop()




