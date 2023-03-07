from scapy.all import *
import tkinter as tk
import tkinter.scrolledtext as tkst
import threading

class NetworkMonitor:
    def __init__(self, master):
        self.master = master
        master.title("Network Monitor")

        # create a label to display captured DNS requests
        self.dns_label = tk.Label(master, text="Captured DNS Requests:")
        self.dns_label.pack()

        # create a scrolled text widget to display the log
        self.log = tkst.ScrolledText(master, height=10, width=50)
        self.log.pack()

        # create a thread to sniff DNS traffic
        self.dns_thread = threading.Thread(target=self.sniff_dns, daemon=True)
        self.dns_thread.start()

    def log_dns_request(self, pkt):
        if pkt.haslayer(DNSQR):
            domain = pkt[DNSQR].qname.decode()
            self.log.insert(tk.END, domain + "\n")
            self.log.see(tk.END)

    def sniff_dns(self):
        sniff(filter="udp port 53", prn=self.log_dns_request)

root = tk.Tk()
app = NetworkMonitor(root)
root.mainloop()
