import tkinter as tk
from tkinter import ttk
import base64
import xml.dom.minidom as minidom

def decode_and_pretty_print():
    # Get the input string from the text box
    input_string = input_text.get("1.0", "end-1c")

    # Decode the input string from base64
    decoded_string = base64.b64decode(input_string).decode("utf-8")

    # Check if the decoded string is valid XML
    try:
        minidom.parseString(decoded_string)
    except Exception:
        # If it's not valid XML, display an error message in the output text box
        output_text.delete("1.0", "end")
        output_text.insert("1.0", "Error: Decoded string is not valid XML.")
        return

    # Pretty print the decoded output
    pretty_output = minidom.parseString(decoded_string).toprettyxml()

    # Update the output text box with the pretty printed output
    output_text.delete("1.0", "end")
    output_text.insert("1.0", pretty_output)

# Create the main window
window = tk.Tk()
window.title("Base64 Decoder and Pretty Printer")

# Create the input label and text box
input_label = ttk.Label(window, text="Enter Base64-encoded XML:")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_text = tk.Text(window, height=5)
input_text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Create a scrollbar for the output text box
output_scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL)

# Create the output label and text box
output_label = ttk.Label(window, text="Decoded and pretty printed output:")
output_label.grid(row=2, column=0, padx=5, pady=5)
output_text = tk.Text(window, height=10, yscrollcommand=output_scrollbar.set)
output_text.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
output_scrollbar.config(command=output_text.yview)
output_scrollbar.grid(row=3, column=1, sticky="ns")

# Create the decode button
decode_button = ttk.Button(window, text="Decode and Pretty Print", command=decode_and_pretty_print)
decode_button.grid(row=4, column=0, padx=5, pady=5)

# Configure the grid to resize the output text box when the window is resized
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(3, weight=1)

# Start the main event loop
window.mainloop()
