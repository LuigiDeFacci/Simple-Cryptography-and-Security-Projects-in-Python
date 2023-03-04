import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet


# Define the secret key for encryption and decryption
key = b'our_secret_key_here' #Fernet key must be 32 url-safe base64-encoded bytes.
fernet = Fernet(key)


# Define the PasswordManager class
class PasswordManager:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Manager")

        # Create the input fields and labels
        tk.Label(self.window, text="Website: ").grid(row=0, column=0)
        self.website_entry = tk.Entry(self.window)
        self.website_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Username: ").grid(row=1, column=0)
        self.username_entry = tk.Entry(self.window)
        self.username_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Password: ").grid(row=2, column=0)
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.grid(row=2, column=1)

        # Create the buttons
        tk.Button(self.window, text="Add", command=self.add_password).grid(row=3, column=0)
        tk.Button(self.window, text="View", command=self.view_passwords).grid(row=3, column=1)
        tk.Button(self.window, text="Edit", command=self.edit_password).grid(row=4, column=0)
        tk.Button(self.window, text="Delete", command=self.delete_password).grid(row=4, column=1)

        self.window.mainloop()

    def add_password(self):
        # Get the user input
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Encrypt the password
        encrypted_password = fernet.encrypt(password.encode())

        # Save the password to a file
        with open("passwords.txt", "a") as f:
            f.write(f"{website} | {username} | {encrypted_password.decode()}\n")

        # Clear the input fields
        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

        # Display a success message
        messagebox.showinfo("Success", "Password added successfully")

    def view_passwords(self):
        # Read the passwords from the file
        try:
            with open("passwords.txt", "r") as f:
                passwords = f.readlines()
        except FileNotFoundError:
            passwords = []

        # Decrypt and display the passwords
        password_list = []
        for password in passwords:
            website, username, encrypted_password = password.split(" | ")
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
            password_list.append(f"{website} | {username} | {decrypted_password}")
            messagebox.showinfo("Passwords", "\n".join(password_list))

    def edit_password(self):
        # Get the user input
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Encrypt the password
        encrypted_password = fernet.encrypt(password.encode())

        # Read the passwords from the file and update the specified password
        with open("passwords.txt", "r") as f:
            passwords = f.readlines()
        with open("passwords.txt", "w") as f:
            for p in passwords:
                if website in p:
                    p = f"{website} | {username} | {encrypted_password.decode()}\n"
                f.write(p)

        # Clear the input fields
        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
            # Display a success message
        messagebox.showinfo("Success", "Password edited successfully")

    def delete_password(self):
        # Get the user input
        website = self.website_entry.get()

        # Read the passwords from the file and remove the specified password
        with open("passwords.txt", "r") as f:
            passwords = f.readlines()
        with open("passwords.txt", "w") as f:
            for p in passwords:
                if website not in p:
                    f.write(p)

        # Clear the input fields
        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

        # Display a success message
        messagebox.showinfo("Success", "Password deleted successfully")

if __name__ == '__main__':
    PasswordManager()
