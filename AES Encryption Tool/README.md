<!DOCTYPE html>
<html> 
  <body>
    <h1>AES Encryption Tool</h1>
    <p>The Encryption Tool is a simple Python program that allows you to encrypt and decrypt files using a symmetric encryption algorithm (AES) and a user-specified encryption key. The program uses the <code>cryptography</code> library to perform the encryption and decryption.</p>
<h2>Installation</h2>
<p>To use the Encryption Tool, you will need to have Python 3 and the <code>cryptography</code> library installed on your computer. You can install <code>cryptography</code> using pip:</p>
<pre><code>pip install cryptography</code></pre>
<p>To run the program, simply navigate to the directory containing the program files and run the <code>encryption_tool.py</code> script:</p>
<pre><code>python encryption_tool.py</code></pre>

<h2>Usage</h2>
<p>When you run the program, a GUI window will appear with two buttons: "Encrypt" and "Decrypt". To encrypt a file, click the "Encrypt" button and select the file you want to encrypt using the file dialog. You will also be prompted to enter an encryption key.</p>
<p>To decrypt a file, click the "Decrypt" button and select the encrypted file you want to decrypt using the file dialog. You will again be prompted to enter the encryption key.</p>
<p>Note that the encryption key is not stored anywhere in the program, so you will need to remember the key used to encrypt a file in order to decrypt it later.</p>

<h2>Security</h2>
<p>The Encryption Tool uses a strong symmetric encryption algorithm (AES) to encrypt and decrypt files, which should provide a high level of security if a strong encryption key is used. However, no encryption method is completely foolproof, and it is always possible that a determined attacker could find a way to decrypt the encrypted file.</p>
<p>It is important to choose a strong encryption key (e.g., a long, random string of characters) and to keep the key secret. It is also a good practice to store the encrypted file and the key separately, and to use additional security measures (such as a password-protected computer or a secure storage device) to protect the encrypted file and key from unauthorized access.</p>

<h2>Acknowledgments</h2>
<p>This program was created as a programming exercise, and was inspired by similar encryption tools and tutorials available online. The <code>cryptography</code> library was used to implement the encryption and decryption functionality.</p>
  </body>
</html>
