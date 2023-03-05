import tkinter as tk
import tkinter.messagebox as messagebox
import pyperclip
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class App:
    def __init__(self, master):
        self.master = master
        master.title("AES Key Generator")
        
        self.key_length_var = tk.StringVar(value="128 bits")
        self.key_length_options = ["32 bits", "64 bits", "96 bits", "128 bits", "192 bits", "256 bits"]

        # Create a "Key Length" option menu
        key_length_label = tk.Label(master, text="Key Length:")
        key_length_label.pack()
        self.key_length_menu = tk.OptionMenu(master, self.key_length_var, *self.key_length_options)
        self.key_length_menu.pack()
        
        # Create a "Generate Key" and "Copy Key to Clipboard" option menu
        self.generate_button = tk.Button(master, text="Generate Key", command=self.generate_key)
        self.generate_button.pack()

        self.copy_button = tk.Button(master, text="Copy Key to Clipboard", command=self.copy_key)
        self.copy_button.pack()

    def generate_key(self):
        key_length_str = self.key_length_var.get()
        key_length = int(key_length_str.split()[0]) // 8
        key = get_random_bytes(key_length)
        messagebox.showinfo("Key Generated", f"AES key ({key_length*8} bits) successfully generated!")
        self.key = key

    def copy_key(self):
        try:
            pyperclip.copy(self.key.hex())
            messagebox.showinfo("Key Copied", "AES key successfully copied to clipboard!")
        except AttributeError:
            messagebox.showerror("No Key Generated", "Please generate an AES key first.")

class CustomKeyLengthDialog:
    def __init__(self, parent):
        self.result = None

        self.top = tk.Toplevel(parent)
        self.top.title("Custom Key Length")

        self.length_label = tk.Label(self.top, text="Key Length (in bytes):")
        self.length_label.pack()

        self.length_entry = tk.Entry(self.top)
        self.length_entry.pack()

        self.ok_button = tk.Button(self.top, text="OK", command=self.ok)
        self.ok_button.pack()

    def ok(self):
        try:
            key_length = int(self.length_entry.get())
            if key_length < 1 or key_length % 8 != 0:
                raise ValueError("Key length must be a multiple of 8 bytes")
            self.result = key_length
            self.top.destroy()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer for key length (must be a multiple of 8 bytes)")

root = tk.Tk()
app = App(root)
root.mainloop()
