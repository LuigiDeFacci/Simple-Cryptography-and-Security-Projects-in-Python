import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet

class EncryptionTool:
    def __init__(self, master):
        self.master = master
        self.master.title("Encryption Tool")

        # Create buttons
        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack(pady=10)
        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack(pady=10)

        # Initialize key
        self.key = None

    def select_file(self):
        # Open file dialog to select file
        file_path = filedialog.askopenfilename()
        return file_path

    def get_key(self):
        # Get key from user
        key = tk.simpledialog.askstring("Key", "Enter encryption key:")
        return key.encode()

    def encrypt(self):
        # Get key from user
        key = self.get_key()

        # Select file to encrypt
        file_path = self.select_file()

        # Read file contents
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Encrypt file contents
        f = Fernet(key)
        encrypted_data = f.encrypt(file_data)

        # Write encrypted data to file
        with open(file_path + '.encrypted', 'wb') as file:
            file.write(encrypted_data)

        # Show success message
        tk.messagebox.showinfo("Success", "File encrypted successfully!")

    def decrypt(self):
        # Get key from user
        key = self.get_key()

        # Select file to decrypt
        file_path = self.select_file()

        # Read file contents
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Decrypt file contents
        f = Fernet(key)
        try:
            decrypted_data = f.decrypt(file_data)
        except:
            tk.messagebox.showerror("Error", "Invalid key. Please enter the correct key.")
            return

        # Write decrypted data to file
        with open(file_path[:-10], 'wb') as file:
            file.write(decrypted_data)

        # Show success message
        tk.messagebox.showinfo("Success", "File decrypted successfully!")


root = tk.Tk()
encryption_tool = EncryptionTool(root)
root.mainloop()
