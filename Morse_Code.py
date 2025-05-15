import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Morse Code Converter")
root.geometry("600x400")

enmorse = {
    "a": "-", "b": "-", "c": "--", "d": "-", "e": "*",
    "f": "-", "g": "--", "h": "", "i": "", "j": "*---",
    "k": "--", "l": "-", "m": "--", "n": "-*", "o": "---",
    "p": "--", "q": "---", "r": "-", "s": "", "t": "-",
    "u": "-", "v": "-", "w": "--", "x": "--", "y": "-*--",
    "z": "--", "0": "-----", "1": "----", "2": "---", "3": "--",
    "4": "-", "5": "", "6": "-", "7": "--", "8": "---",
    "9": "----*", " ": "|"
}

demorse = {v: k for k, v in enmorse.items()}

def encrypt():
    text = input_text.get("1.0", tk.END).strip().lower()
    output = ""
    for char in text:
        if char in enmorse:
            output += enmorse[char] + " "
        else:
            output += "? "
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output.strip())

def decrypt():
    code = input_text.get("1.0", tk.END).strip().split()
    output = ""
    for symbol in code:
        if symbol == "|":
            output += " "
        elif symbol in demorse:
            output += demorse[symbol]
        else:
            output += "?"
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)

input_label = tk.Label(root, text="Enter text or Morse code:")
input_label.pack()

input_text = tk.Text(root, height=5, width=60)
input_text.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(pady=5)

output_label = tk.Label(root, text="Result:")
output_label.pack()

output_text = tk.Text(root, height=5, width=60)
output_text.pack()

root.mainloop()