# loadAndExploreCSV.py
# This script loads a CSV file containing network traffic data and explores its contents.

# Imports
import pandas as pd
import matplotlib.pyplot as plt


# Load the CSV file into a DataFrame
df = pd.read_csv('traffic_capture.csv')

# Display basic information about the DataFrame
print("DataFrame Information:") 
print(df.info())
print(df.head())

# Check unique protocols in the DataFrame
print("\nUnique Protocols:", df['protocol'].nunique())

# Plot protocol distribution
protocol_counts = df['protocol'].value_counts()
protocol_counts.plot(kind='bar', title='Protocol Distribution')
plt.xlabel('Protocol')
plt.ylabel('Count')
plt.show()

df['length'].plot(kind='hist', bins=50, title='Packet Length Distribution')
plt.xlabel('Packet Length (bytes)')
plt.show()