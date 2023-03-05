<!DOCTYPE html>
<html>
  <body>
    <h1>AES Key Generator</h1>
    <p>This program generates a random AES encryption key and allows the user to copy the key to the clipboard. The key length can be selected from a list of predefined options or a custom key length can be entered.</p>
    <h2>Dependencies</h2>
    <ul>
      <li>tkinter</li>
      <li>pyperclip</li>
      <li>Crypto (from pycryptodome package)</li>
    </ul>
    <h2>How to use</h2>
    <ol>
      <li>Run the program.</li>
      <li>Select the desired key length from the "Key Length" option menu.</li>
      <li>Click the "Generate Key" button to generate a random key.</li>
      <li>Click the "Copy Key to Clipboard" button to copy the key to the clipboard.</li>
      <li>If the desired key length is not in the predefined options, click the "Custom Key Length" button to enter a custom key length.</li>
    </ol>
    <h2>Classes</h2>
    <h3>App</h3>
    <p>This is the main class that creates the GUI and handles the key generation and copying to clipboard.</p>
    <h4>Methods</h4>
    <ul>
      <li><code>__init__(self, master)</code>: Initializes the GUI with the "Key Length" option menu, "Generate Key" button, and "Copy Key to Clipboard" button.</li>
      <li><code>generate_key(self)</code>: Generates a random AES encryption key with the length specified by the "Key Length" option menu.</li>
      <li><code>copy_key(self)</code>: Copies the generated key to the clipboard.</li>
      <li><code>CustomKeyLengthDialog</code>: Creates a dialog box for entering a custom key length.</li>
    </ul>
    <h3>CustomKeyLengthDialog</h3>
    <p>This class creates a dialog box for entering a custom key length.</p>
    <h4>Methods</h4>
    <ul>
      <li><code>__init__(self, parent)</code>: Initializes the dialog box with a label and entry box for entering the key length, and an "OK" button for submitting the key length.</li>
      <li><code>ok(self)</code>: Validates the entered key length and stores the result. If the entered key length is invalid, an error message is displayed.</li>
    </ul>
  </body>
</html>
