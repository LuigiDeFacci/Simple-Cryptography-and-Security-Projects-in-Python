<!DOCTYPE html>
<html>
<body>
	<h1>Network Traffic Monitor</h1>
	<p>This program allows you to monitor network traffic on the device the program is running on. It captures packets and displays information about the source and destination MAC addresses, IP addresses, ports, protocol, payload, and time of each packet.</p>
<h2>Dependencies</h2>
<ul>
	<li>Python 3.x</li>
	<li>Scapy</li>
	<li>Tkinter</li>
</ul>

<h2>Usage</h2>
<p>To run the program, execute the following command:</p>

<pre><code>python network_monitor.py</code></pre>

<p>When the program starts, click the "Start" button to begin capturing packets. The program will capture packets for 10 seconds by default, but you can modify this in the code if you wish. The program will display information about each packet in the text area. Click the "Stop" button to stop capturing packets.</p>

<p>After capturing packets, click the "Save" button to save the captured information to a text file.</p>

<h2>Packet Information</h2>
<p>The following information is captured for each packet:</p>
<ul>
	<li>Source MAC address</li>
	<li>Destination MAC address</li>
	<li>Protocol</li>
	<li>Payload (if applicable)</li>
	<li>Time</li>
</ul>
</body>
</html>
