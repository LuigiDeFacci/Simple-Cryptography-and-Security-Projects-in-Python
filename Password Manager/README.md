<!DOCTYPE html>
<html>
<body>
	<h1>Password Manager</h1>
	<p>The Password Manager is a Python program that allows you to store and manage your passwords securely. It uses the Fernet encryption algorithm from the <code>cryptography</code> library to encrypt and decrypt passwords, ensuring that they are not stored in plain text.</p>
	<h2>How to Use</h2>
<p>To use the Password Manager:</p>
<ol>
	<li>Make sure you have Python installed on your computer.</li>
	<li>Install the <code>tkinter</code> and <code>cryptography</code> libraries. You can do this using pip:</li>
	<pre><code>pip install tkinter cryptography</code></pre>
	<li>Copy and paste the code from the <code>password_manager.py</code> file into a new Python file.</li>
	<li>Replace the <code>key</code> variable with your own secret key. The key must be 32 url-safe base64-encoded bytes. You can generate a key using the following code:</li>
	<pre><code>from cryptography.fernet import Fernet key = Fernet.generate_key()
print(key)</code></pre>
<li>Save the file and run it.</li>
</ol>
<h2>Features</h2>
<p>The Password Manager has the following features:</p>
<ul>
	<li>Add a new password: Enter the website, username, and password and click the "Add" button to save the password to a file.</li>
	<li>View saved passwords: Click the "View" button to display a list of saved passwords.</li>
	<li>Edit a password: Enter the website, username, and new password and click the "Edit" button to update a saved password.</li>
	<li>Delete a password: Enter the website and click the "Delete" button to remove a saved password.</li>
</ul>
<p>The Password Manager has the following features:</p>
<ul>
	<li>Add a new password: Enter the website, username, and password and click the "Add" button to save the password to a file.</li>
	<li>View saved passwords: Click the "View" button to display a list of saved passwords.</li>
	<li>Edit a password: Enter the website, username, and new password and click the "Edit" button to update a saved password.</li>
	<li>Delete a password: Enter the website and click the "Delete" button to remove a saved password.</li>
</ul>
</body>
</html>
