import tkinter as tk
from scapy.all import *


class NetworkMonitor:
    def __init__(self, master):
        self.master = master
        self.master.title("Network Traffic Monitor")

        # create start and stop buttons
        self.start_button = tk.Button(self.master, text="Start", command=self.start_monitoring)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_monitoring, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT)
        
        # create save button
        self.save_button = tk.Button(self.master, text="Save", command=self.save_results, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT)

        # create text area to display results
        self.text_area = tk.Text(self.master)
        self.text_area.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

        # set up packet capture
        self.capture = None
        self.is_monitoring = False
        self.packets = []

    def start_monitoring(self):
        # open default device in promiscuous mode
        self.capture = sniff(timeout=10, prn=self.process_packet)  # capture packets for 10 seconds
        self.is_monitoring = True

        # change button states
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_monitoring(self):
        # stop packet capture and change button states
        self.is_monitoring = False
        self.capture = None
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.NORMAL)

    def process_packet(self, packet):
        # process packet information
        if packet.haslayer(Ether):
            source_mac = packet[Ether].src
            dest_mac = packet[Ether].dst
            packet_time = packet.time
            payload = packet.payload
            self.packets.append(f"Time: {packet_time}, Source MAC: {source_mac}, Dest MAC: {dest_mac}, Payload: {payload}\n")
            self.text_area.insert(tk.END, f"Time: {packet_time}, Source MAC: {source_mac}, Dest MAC: {dest_mac}, Payload: {payload}\n")
            self.text_area.see(tk.END)  # scroll to bottom of text area

    def save_results(self):
        # save packet information to a file
        with open("packet_info.txt", "w") as f:
            f.writelines(self.packets)

        # change button state
        self.save_button.config(state=tk.DISABLED)


if __name__ == '__main__':
    root = tk.Tk()  # create main window
    app = NetworkMonitor(root)  # create NetworkMonitor instance
    root.mainloop()  # start main event loop
