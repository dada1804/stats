 import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("AusAntidiabeticDrug.csv")

# Convert the 'ds' column to datetime
df['ds'] = pd.to_datetime(df['ds'])

# Set the style and color of the plot
sns.set(style='whitegrid', color_codes=True)

# Create the line plot
plt.figure(figsize=(16, 6))
plt.plot(df['ds'], df['y'])
plt.xlabel('Time')
plt.ylabel('Sales ($millions)')
plt.title('Sales of Anti-Diabetic Drug')
plt.show()
