<!DOCTYPE html>
<html>
  <body>
    <h1>Random Password Generator</h1>
    <p>This program generates a random password of a fixed length and displays it on a label. The password is generated by combining uppercase letters, lowercase letters, digits, and symbols.</p>
    <h2>Requirements</h2>
<p>This program requires the following modules:</p>
<ul>
  <li><code>random</code>: to generate random values.</li>
  <li><code>string</code>: to get predefined sets of characters.</li>
  <li><code>tkinter</code>: to create the GUI.</li>
  <li><code>pyperclip</code>: to copy and paste text to and from the clipboard.</li>
</ul>

<h2>Constants</h2>
<p>The program uses the following constants:</p>
<ul>
  <li><code>PASSWORD_LENGTH</code>: the length of the password to be generated.</li>
  <li><code>UPPERCASE_CHARS</code>: a string containing all uppercase letters.</li>
  <li><code>LOWERCASE_CHARS</code>: a string containing all lowercase letters.</li>
  <li><code>DIGITS</code>: a string containing all digits from 0 to 9.</li>
  <li><code>SYMBOLS</code>: a string containing all punctuation symbols.</li>
  <li><code>ALL_CHARS</code>: a list containing all possible characters for the password.</li>
</ul>

<h2>Functionality</h2>
<p>The program defines a function <code>generate_password()</code> that generates a random password and displays it on the label. The function works as follows:</p>
<ol>
  <li>Create an empty password string.</li>
  <li>Choose a random uppercase letter and add it to the password.</li>
  <li>Choose a random lowercase letter and add it to the password.</li>
  <li>Choose a random digit and add it to the password.</li>
  <li>Choose a random symbol and add it to the password.</li>
  <li>Fill the remaining characters with random choices from all possible characters.</li>
  <li>Shuffle the password to make it more unpredictable.</li>
  <li>Display the password on the label and copy it to the clipboard.</li>
</ol>

<h2>User Interface</h2>
<p>The program creates a root window with a title "Random Password Generator" and a size of 500x100 pixels. It then creates a button "Generate Password" that calls the <code>generate_password()</code> function when clicked. A label is also created that initially shows an empty string, but is updated with the generated password when the button is clicked. The generated password is also copied to the clipboard.</p>

<h2>How to Run</h2>
<p>To run the program, execute the Python file <code>random_password_generator.py</code>. This will open the GUI window. Click the "Generate Password" button to generate a new password. The password will be displayed on the label and copied to the clipboard.</p>
