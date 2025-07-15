# capturePackets.py
# This script captures network traffic for 10 seconds and saves the parsed packets to a CSV file.

#Imports
import pyshark 
import pandas as pd

# Configuration of the capture
capture = pyshark.LiveCapture(interface='Wi-Fi', output_file='capture.pcap')

print("Starting capture for 10 seconds... Press Ctrl+C to stop.")

# Start the capture for 10 secs
capture.sniff(timeout=10)

print("Capture complete. Processing packets...")

# Process the captured packets and save to CSV
cap = pyshark.FileCapture('capture.pcap')

# Initialize a list to hold packet data
data = []

# Iterate through the captured packets and extract relevant information
for packet in cap:
    try: 
        data.append({
            'timestamp': packet.sniff_time,
            'length': packet.length,
            'protocol': packet.highest_layer,
            'src': packet.ip.src if hasattr(packet, 'ip') else None,
            'dst': packet.ip.dst if hasattr(packet, 'ip') else None,
        })
    except AttributeError:
        continue
    
# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('traffic_capture.csv', index=False)

print("Saved parsed packets to traffic_capture.csv")