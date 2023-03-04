import re
import tkinter as tk

def check_password_strength(password):
    # Define regex patterns to match different types of characters
    digit_pattern = re.compile(r'\d')
    uppercase_pattern = re.compile(r'[A-Z]')
    lowercase_pattern = re.compile(r'[a-z]')
    symbol_pattern = re.compile(r'[!@#$%^&*()_+=-`~{}|\[\]:";\'<>?,./]')

    # Check password length
    if len(password) < 8:
        return 'Password is too short'

    # Check if password contains required characters
    if not digit_pattern.search(password):
        return 'Password must contain at least one digit'
    if not uppercase_pattern.search(password):
        return 'Password must contain at least one uppercase letter'
    if not lowercase_pattern.search(password):
        return 'Password must contain at least one lowercase letter'
    if not symbol_pattern.search(password):
        return 'Password must contain at least one symbol'

    # Password meets all criteria
    return 'Password is strong'

def check_password():
    # Get password from input field
    password = password_entry.get()

    # Check password strength
    result = check_password_strength(password)

    # Update output label with result
    output_label.config(text=result)

# Create GUI window
window = tk.Tk()
window.title('Password Strength Checker')

# Create input label and field
password_label = tk.Label(window, text='Enter password:')
password_label.pack()
password_entry = tk.Entry(window, show='*')
password_entry.pack()

# Create button to check password
check_button = tk.Button(window, text='Check', command=check_password)
check_button.pack()

# Create output label
output_label = tk.Label(window, text='')
output_label.pack()

# Start GUI event loop
window.mainloop()
