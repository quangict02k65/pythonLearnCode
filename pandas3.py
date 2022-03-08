#SUMMARY FUNCTIONS AND MAPS 

import pandas as pd
import numpy as np

reviews  = pd.read_csv(r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\winemag-data-130k-v2.csv", index_col= 0 )
option1 = pd.set_option('max_rows', 5)

#pandas provides many simple "summary functions " which 
#restructure the data in some useful way 
#describe() method
'''
This method generates a high-level summary of the attributes of the given column. 
It is type-aware, meaning that its output changes based on the data type of the input.
 The output above only makes sense for numerical data; 
 for string data here's what we get
'''
point_describe  = reviews.points.describe()
print(point_describe)
# count    129971.000000
# mean         88.447138
#              ...
# 75%          91.000000
# max         100.000000

taster_name_describe = reviews.taster_name.describe()
print(taster_name_describe)
# count         103727
# unique            19
# top       Roger Voss
# freq           25514

#có một số hàm cơ bản thống kê in dataframe and series
#example
means = reviews.points.mean()
#in ra điểm trung bình 
print(means)
#hàm unique: in ra một list các giá trị chuỗi khác nhau 

unique_name = reviews.taster_name.unique()
print(unique_name)
# ['Kerin O’Keefe' 'Roger Voss' 'Paul Gregutt' 'Alexander Peartree'
#  'Michael Schachner' 'Anna Lee C. Iijima' 'Virginie Boone' 'Matt Kettmann'
#  nan 'Sean P. Sullivan' 'Jim Gordon' 'Joe Czerwinski'
#  'Anne Krebiehl\xa0MW' 'Lauren Buzzeo' 'Mike DeSimone' 'Jeff Jenssen'
#  'Susan Kostrzewa' 'Carrie Dykes' 'Fiona Adams' 'Christina Pickard']

#methods value_counts
#đếm số lần mỗi chuỗi xảy ra 

count_value = reviews.taster_name.value_counts()
print(count_value)


#MAPS
'''
a map  is a term , borrowed from mathematics , for a function that takes one set of values and "maps
 them to another set of values. In data science we often have a need for creating new representations
 from existing data , or for transforming data from the format it is in now to the format that we 
 want it to be in later. Maps are what handle this work , making them extremely important 
 for getting your work done'''

 #there are two mapping methods that we will use often 
 #map() is the first,and slightly simpler one
 #lambda là một hàm vô danh được sử dụng trong thời gian ngắn
 #nó thường được sử dụng với các hàm tích hợp sẵn trong pythn như filter hay map
review_points_mean = reviews.points.mean()
print("gia tri trung binh la : ", review_points_mean)
map1 = reviews.points.map(lambda p: p - review_points_mean)
print(map1)
print(reviews['points'])
# 0        -1.447138
# 1        -1.447138
#             ...
# 129969    1.552862
# 129970    1.552862
#map trả về một phiên bản đã biến đổi của giá trị

#tương tự với nó là phương thức apply()
#note that: map() return new transformed series
#apply() return new transformed dataframes

print(reviews.describe())
def remean_points(row):
    row.points = row.points - review_points_mean
    return row
apply1 = reviews.apply(remean_points, axis='columns')
print(apply1['points'])

'''
if we had called reviews.apply() with axis = 'index', then instead of passing a func
to transform each row, we would need to give a funcetion to transform each column
'''
'''
they don't modify the original data they are called on
khi nhìn vào hàng đầu tien thì dữ liệu ban đầu không hề thay đổi 
'''


region1 = reviews.country + "-" + reviews.region_1
print(region1)
# 0            Italy-Etna
# 1                   NaN
#               ...
# 129969    France-Alsace
# 129970    France-Alsace


'''
python hiểu bạn thao tác một series với một số
và nó cũng hiểu bạn thao tác một series với một series khác 
Dùng map và apply thì nó có thẻ thực hiện nhiều thao tác nâng cao hơn
ví dụ như conditional logic còn các phép +- bình thường k thể
'''
'''
nhìn chung lại thì map và apply khoogn làm thay đổi dataframe gốc của mình
nó chỉ đưa ra cho chúng ta tính toán 
'''
