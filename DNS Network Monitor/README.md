<!DOCTYPE html>
<html>
<body>
    <h1>DNS Network Monitor</h1>
    <p>This program is a simple network monitoring tool built using the <code>scapy</code> packet manipulation library and the <code>tkinter</code> GUI toolkit. </p>
    <p>When the program is run, it creates a window displaying a label that reads "Captured DNS Requests" and a scrolled text widget that displays the captured DNS requests.</p>
    <p>The <code>NetworkMonitor</code> class is responsible for creating and managing the window and the <code>sniff_dns</code> method is responsible for capturing DNS requests.</p>
    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>scapy</code> library</li>
        <li><code>tkinter</code> library</li>
    </ul>
    <h2>Usage</h2>
    <ol>
        <li>Install the required libraries:
            <pre>pip install scapy tkinter</pre>
        </li>
        <li>Run the program:
            <pre>python network_monitor.py</pre>
        </li>
        <li>The program window will open, and captured DNS requests will be displayed in the scrolled text widget.</li>
    </ol>
    <h2>Class Methods</h2>
    <h3><code>__init__(self, master)</code></h3>
    <p>The constructor method for the <code>NetworkMonitor</code> class. It initializes the window and creates the necessary widgets.</p>
    <h3><code>log_dns_request(self, pkt)</code></h3>
    <p>A method that takes a packet object and extracts the DNS request from it. It then logs the domain name to the scrolled text widget.</p>
    <h3><code>sniff_dns(self)</code></h3>
    <p>A method that captures DNS traffic on port 53 using the <code>sniff</code> function from the <code>scapy</code> library. It calls the <code>log_dns_request</code> method for each captured packet.</p>
      
</body>
</html>
