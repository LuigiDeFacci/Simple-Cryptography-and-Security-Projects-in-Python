<!DOCTYPE html>
<html>
  <body>
    <h1>Caesar Cipher Decryptor</h1>
    <p>This Python program implements a GUI window for decrypting messages using the Caesar cipher algorithm. It provides a simple and intuitive interface for users to input a ciphertext and a key, and then obtain the corresponding plaintext.</p>
    <h2>Dependencies</h2>
    <p>This program requires the <code>tkinter</code> module, which is included in the standard library of Python 3.</p>
    <h2>Usage</h2>
    <p>To use this program, simply run the <code>main()</code> function. A GUI window will appear, with two input fields and a "Decrypt" button.</p>
    <p>The first input field is for the ciphertext, which should be entered as a string. The second input field is for the key, which should be entered as an integer. If no key is provided, the default key of 3 will be used.</p>
    <p>Once the user clicks the "Decrypt" button, the plaintext will be displayed in the third input field, which is read-only. If the user wishes to decrypt another message, they can simply clear the input fields and enter a new ciphertext and/or key.</p>
    <h2>Functionality</h2>
    <p>The <code>decrypt_caesar</code> function takes a ciphertext and a key as input, and returns the corresponding plaintext. It uses the Caesar cipher algorithm, which involves shifting each letter in the ciphertext by the key value, with wraparound if necessary. The algorithm preserves the case of each letter, and leaves all non-letter characters unchanged.</p>
    <p>The <code>DecryptWindow</code> class defines the layout and behavior of the GUI window. It inherits from the <code>tkinter.Frame</code> class, and contains several <code>tkinter</code> widgets such as labels, entry fields, and a button. The <code>decrypt</code> method is called when the user clicks the "Decrypt" button, and it retrieves the input values, calls the <code>decrypt_caesar</code> function, and updates the third input field with the resulting plaintext.</p>
    <p>The <code>main</code> function creates an instance of the <code>DecryptWindow</code> class and passes it to the <code>tkinter.Tk</code> constructor, which initializes the main window of the GUI. The <code>mainloop</code> method is then called to start the event loop, which waits for user input and updates the GUI as necessary.</p>
  </body>
</html>
