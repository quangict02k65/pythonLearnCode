#CREATING, READING AND WRITING IN PANDAS

import pandas as pd


# #there are two core objects in pandas: DataFrame and series
# #DataFrame is a table 
# table1 = pd.DataFrame({'quang':[3,4,5,23], 'quynh' : [3,45,42,43]})
# print(table1)

# #The list of row labels used in a dataframe is index(tên của hàng gọi là index)

# table2 = pd.DataFrame({'rooney':['manchester united'], 'ronaldo': ['real madrid']}, index=['club'])
# print(table2)
# #    quang  quynh
# # 0      3      3
# # 1      4     45
# # 2      5     42
# # 3     23     43
# #                  rooney      ronaldo
# # club  manchester united  real madrid

# #series : is a sequence of data values
# #if dataframe is a table , a series is a list 

# seri1 = pd.Series([1,2,3,4,5,6,7])
# print(seri1)
# seri2 = pd.Series([34,53,23], index = ['so1', 'so2', 'so3'], name = 'product 1')
# print(seri2)
# so1    34
# so2    53
# so3    23
# Name: product 1, dtype: int64
#một dataframe chỉ là một loạt các series dán lại với nhau 
#hai cái liên quan mật thiết với nhau .

#READING DATA FILES 
#by far the most basic of these is the CSV file
#a CSV file is a table of values separated by commas. Comma-Seperated Values
#(một bảng giá trị ngăn cách nhau bởi dấu phẩy )

#pd.read_csv() func to read the data into a Dataframe
wine_reviews = pd.read_csv(r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\winemag-data-130k-v2.csv")

#shape attribute check hơ large the resulting datafram( số hàng, số cột)
sha = wine_reviews.shape
print(sha)
# (129971,14)

#head( ) command grabs the first five rows(in thông tin 5 hàng đầu tiên)
print(wine_reviews.head())


wine_reviews2 = pd.read_csv(r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\winemag-data-130k-v2.csv",index_col = 0)
print(wine_reviews2.head())
#thêm cái index_col đằng sau là bỏ  đi cột thứ 0 trong dataset



