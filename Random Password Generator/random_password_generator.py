# Import modules
import random
import string
import tkinter as tk
import pyperclip # Module for copying and pasting text to and from the clipboard

# Define constants
PASSWORD_LENGTH = 15 # Length of the password
UPPERCASE_CHARS = string.ascii_uppercase # Uppercase letters
LOWERCASE_CHARS = string.ascii_lowercase # Lowercase letters
DIGITS = string.digits # Digits from 0 to 9
SYMBOLS = string.punctuation # Punctuation symbols

# Create a list of all possible characters
ALL_CHARS = list(UPPERCASE_CHARS + LOWERCASE_CHARS + DIGITS + SYMBOLS)

# Define a function that generates a random password and displays it on the label
def generate_password():
    # Create an empty password string
    password = ""

    # Choose a random uppercase letter and add it to the password
    password += random.choice(UPPERCASE_CHARS)

    # Choose a random lowercase letter and add it to the password
    password += random.choice(LOWERCASE_CHARS)

    # Choose a random digit and add it to the password
    password += random.choice(DIGITS)

    # Choose a random symbol and add it to the password
    password += random.choice(SYMBOLS)

    # Fill the remaining characters with random choices from all possible characters
    for i in range(PASSWORD_LENGTH - 4):
        password += random.choice(ALL_CHARS)

    # Shuffle the password to make it more unpredictable
    password = "".join(random.sample(password, len(password)))

    # Display the password on the label and copy it to the clipboard 
    label.config(text="Your password was copied to the clipboard: " + password)
    pyperclip.copy(password) 

# Create a root window with a title and a size 
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x100")

# Create a button that calls the generate_password function when clicked 
button = tk.Button(root, text="Generate Password", command=generate_password)
button.pack()

# Create a label that shows the generated password or an empty string initially  
label = tk.Label(root, text="")
label.pack()

# Start the main loop of the window  
root.mainloop()
