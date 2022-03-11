from cProfile import label
from itertools import filterfalse
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# Path of the file to read
iris_filepath = r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\iris.csv"
iris_data = pd.read_csv(iris_filepath, index_col="Id")

# Print the first 5 rows of the data
print(iris_data.head())


'''HISTOGRAMS (BIỂU ĐỒ)
Histograms are used to show distributions of variables while bar charts are used to compare variables'''
#histogram là biểu đồ thể hiện sự phân phối của các biến trong khoảng gía trị

# sns.distplot(a = iris_data['Petal Length (cm)'], kde = False)
# #kde: kernel density estimate : ước lượng mật độ kernel
# plt.show()


'''DENSITY PLOTS: MẬT ĐỘ (KDE PLOTS)'''
#được coi là phiên ban làm mịn của histograms 

#sns.kdeplot(data = iris_data['Petal Length (cm)'], shade= True)
#shade = True là tô màu phần dưới hàm mật độ 


'''2D KDE PLOTS'''
'''we can create a two-dimensional (2D) KDE plot with the sns.jointplot command'''


# 2D KDE plot
#sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")
#plt.show()



'''COLOR-CODED PLIOTS'''
''' for the next part of the tutorial, we will create plots to understand differences between the species
to accomplish this, we begin by breaking the dataset into three separate files, with one for each species'''

# Paths of the files to read
iris_set_filepath = r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\iris_setosa.csv"
iris_ver_filepath =r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\iris_versicolor.csv"
iris_vir_filepath = r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\iris_virginica.csv"

# Read the files into variables 
iris_set_data = pd.read_csv(iris_set_filepath, index_col="Id")
iris_ver_data = pd.read_csv(iris_ver_filepath, index_col="Id")
iris_vir_data = pd.read_csv(iris_vir_filepath, index_col="Id")

# Print the first 5 rows of the Iris versicolor data
iris_ver_data.head()
# Histograms for each species
# sns.distplot(a=iris_set_data['Petal Length (cm)'], label="Iris-setosa", kde=False)
# sns.distplot(a=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", kde=False)
# sns.distplot(a=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", kde=False)

# # Add title
# plt.title("Histogram of Petal Lengths, by Species")

# # Force legend to appear
# plt.legend() #hiện chú thích cho từng loài hoa phía góc trái của histogram
# plt.show()




# KDE plots for each species
sns.kdeplot(data=iris_set_data['Petal Length (cm)'], label="Iris-setosa", shade=True)
sns.kdeplot(data=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", shade=True)
sns.kdeplot(data=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", shade=True)

# Add title
plt.title("Distribution of Petal Lengths, by Species")
plt.show()

#như vậy nhìn vào histogram này rất dễ để nhận ra rằng petal length nhỏ hơn 2cm
#rất có thẻ sẽ là hoa iris setosa.
#và petal length của hai loài hoa còn lại là gần như giống nhau
