import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

import seaborn as sns



# Path of the file to read
spotify_filepath = r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# Line chart 
#plt.show()

#change the style of the figure to the dark theme
sns.set_style("darkgrid")
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)
plt.show()
