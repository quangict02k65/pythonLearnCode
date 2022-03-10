#VISUALIZATION DATA WITH SEABORN
from cProfile import label
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt

import seaborn as sns

# Path of the file to read
fifa_filepath = r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\fifa.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates= True)
#parse_dates = True là định dạng index là kiểu date
print(fifa_data)
print(type(fifa_data.index))
#<class 'pandas.core.indexes.datetimes.DatetimeIndex'>

#PLOT THE DATA
''' in this corse we will learn about many different plot types
In many cases we will need one line of code to make a chart'''

''' LINECHARTS'''
#set the width and height of the figure
plt.figure(figsize= (16,6))
sns.lineplot(data = fifa_data) #tạo linechart

#PLOT A SUBSET OF THE DATA

plt.figure(figsize=(13,4))

#addtitle
plt.title("Ranking fifa ")

#line charts showing score of national football
#lable là chú thích của mỗi đường kẻ 
sns.lineplot(data= fifa_data['ARG'], label = ' Score of agentina')



''' BARCHARTS AND HEATMAPS '''
#biểu đồ cột
plt.figure(figsize=(10,6))

plt.title("FIFA RANKING ")

sns.barplot(x = fifa_data.index, y = fifa_data['ESP'])

plt.ylabel("Score of ESP")




