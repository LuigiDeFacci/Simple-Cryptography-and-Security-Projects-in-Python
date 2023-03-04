import tkinter as tk


def decrypt_caesar(ciphertext, key):
    """Decrypts a message using the Caesar cipher algorithm with the specified key."""
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            char_code = ord(char) - key
            if char.isupper():
                if char_code < ord('A'):
                    char_code += 26
                elif char_code > ord('Z'):
                    char_code -= 26
            else:
                if char_code < ord('a'):
                    char_code += 26
                elif char_code > ord('z'):
                    char_code -= 26
            plaintext += chr(char_code)
        else:
            plaintext += char
    return plaintext


class DecryptWindow(tk.Frame):
    """GUI window for the decryptographic tool."""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Caesar Cipher Decryptor')
        self.create_widgets()

    def create_widgets(self):
        self.ciphertext_label = tk.Label(self.master, text='Ciphertext:')
        self.ciphertext_label.grid(row=0, column=0)
        self.ciphertext_entry = tk.Entry(self.master, width=40)
        self.ciphertext_entry.grid(row=0, column=1)

        self.key_label = tk.Label(self.master, text='Key:')
        self.key_label.grid(row=1, column=0)
        self.key_entry = tk.Entry(self.master, width=10)
        self.key_entry.grid(row=1, column=1)
        self.key_entry.insert(0, '3')

        self.decrypt_button = tk.Button(self.master, text='Decrypt', command=self.decrypt)
        self.decrypt_button.grid(row=2, column=0)

        self.plaintext_label = tk.Label(self.master, text='Plaintext:')
        self.plaintext_label.grid(row=3, column=0)
        self.plaintext_entry = tk.Entry(self.master, width=40, state='readonly')
        self.plaintext_entry.grid(row=3, column=1)

    def decrypt(self):
        ciphertext = self.ciphertext_entry.get()
        key = int(self.key_entry.get())
        plaintext = decrypt_caesar(ciphertext, key)
        self.plaintext_entry.configure(state='normal')
        self.plaintext_entry.delete(0, tk.END)
        self.plaintext_entry.insert(0, plaintext)
        self.plaintext_entry.configure(state='readonly')


def main():
    """Main function that creates the GUI window."""
    root = tk.Tk()
    app = DecryptWindow(root)
    app.mainloop()


if __name__ == '__main__':
    main()
