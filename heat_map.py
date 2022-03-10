from cProfile import label
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# Path of the file to read
file = r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\flight_delays.csv"
flight_data = pd.read_csv(file, index_col= "Month")
# Set the width and height of the figure

# Set the width and height of the figure

plt.figure(figsize=(14,7))

# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")

# Heatmap showing average arrival delay for each airline by month
#annot = True là ta in giá trị vào mỗi ô vuông
sns.heatmap(data = flight_data, annot= True)

# Add label for horizontal axis
plt.xlabel("Airline")
# Heatmap showing average arrival delay for each airline by month

plt.show()
