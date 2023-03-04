<!DOCTYPE html>
<html>
<body>
	<h1>Password Strength Checker</h1>
	<p>This program checks the strength of a password entered by the user, according to the following criteria:</p>
	<ul>
		<li>Password must be at least 8 characters long</li>
		<li>Password must contain at least one digit</li>
		<li>Password must contain at least one uppercase letter</li>
		<li>Password must contain at least one lowercase letter</li>
		<li>Password must contain at least one symbol</li>
	</ul>
	<p>The program uses regular expressions to match different types of characters in the password, and displays a message indicating whether the password is strong or not.</p>
	<h2>Usage</h2>
	<p>To use the program, simply run the Python script <code>password_strength_checker.py</code>. A graphical user interface (GUI) window will appear, with a text field to enter a password, a "Check" button to check the password, and an output label to display the result.</p>
	<p>Enter a password in the text field and click the "Check" button to check the strength of the password. The output label will display a message indicating whether the password is strong or not.</p>
	<h2>Dependencies</h2>
	<p>The program requires the following dependencies:</p>
	<ul>
		<li><code>re</code> module for regular expressions</li>
		<li><code>tkinter</code> module for GUI</li>
	</ul>
	<p>These dependencies are included in most Python installations by default, so no additional installation should be necessary.</p>
</body>
</html>
