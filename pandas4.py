#GROUPING AND SORTING
import pandas as pd


reviews  = pd.read_csv(r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\winemag-data-130k-v2.csv", index_col= 0 )
option1 = pd.set_option('max_rows', 5)

#map allow us to transform data in a dataframe or serires one value at 
#a time for an entire column
#howerver, often we want to group our data, and then do something specific to
#the group the data is in 
#we do this with the groupby() operation 
group1 = reviews.groupby('points')['points'].count()
print(group1)


#chọn ra giá loại rượu rẻ nhất cho mỗi điểm giá trị 
group2 = reviews.groupby('points')['price'].min()
print(group2)

#chúng ta có thể thao tác dữ liệu theo các cách bất kì mà ta thấy phù hợp
#tìm ra tên loại rượu đầu tiên được đánh giá trong mỗi nhà máy rượu trong dataset
group3 = reviews.groupby('winery').apply(lambda df: df.title.iloc[0])
print(group3)
# winery
# 1+1=3                          1+1=3 NV Rosé Sparkling (Cava)
# 10 Knots                 10 Knots 2010 Viognier (Paso Robles)
#                                   ...
# àMaurice    àMaurice 2013 Fred Estate Syrah (Walla Walla V...
# Štoka                         Štoka 2009 Izbrani Teran (Kras)


#in ra loại rượu điểm cao nhất theo country và province
group4 = reviews.groupby(['country', 'province']).apply(lambda df : df.loc[df.points.idxmax()])
print(group4)
#                               country                                        description  ...                variety                winery
# country   province                                                                        ...
# Argentina Mendoza Province  Argentina  If the color doesn't tell the full story, the ...  ...                 Malbec  Bodega Catena Zapata      
#           Other             Argentina  Take note, this could be the best wine Colomé ...  ...                 Malbec                Colomé      
# ...                               ...                                                ...  ...                    ...                   ...      
# Uruguay   San Jose            Uruguay  Baked, sweet, heavy aromas turn earthy with ti...  ...              Red Blend        Castillo Viejo      
#           Uruguay             Uruguay  Cherry and berry aromas are ripe, healthy and ...  ...  Tannat-Cabernet Franc               Narbona  

# print(reviews['title'])


#một phương thức phổ biến của groupby là agg() cho phép chúng ta có kể thống kê một lúc nhiều thông tin 
#ví dụ

group5 = reviews.groupby('country')['price'].agg([len, min, max])
print(group5)
            # len   min    max
# country
# Argentina  3800   4.0  230.0
# Armenia       2  14.0   15.0
# ...         ...   ...    ...
# Ukraine      14   6.0   13.0
# Uruguay     109  10.0  130.0

#tìm theo country và province ra những loại rượu có điểm cao nhất.
group6 = reviews.groupby(['country', 'province'])['points'].agg([max])
print(group6)
print(type(group6.index))

#                             max
# country   province
# Argentina Mendoza Province   97
#           Other              95
# ...                         ...
# Uruguay   San Jose           87
#           Uruguay            91



#MULTI-INDEXES
print(group6.reset_index())
print(group6.reset_index().loc[0,'country'])
#argentina
#phương thức reset_index là cấp lại chỉ mục cho dataframe mà ta vừa tạo ra.


#SORTING
'''
looking again at group6 we can see that grouping returns data in index order, not in value order
that is to say , when outputing the result of a groupby, the order of the rows is dependent on the values
in thes index, not in the data 
to get data in the order want it in we can sort it ourselves. THe sort_value() method is handy for this
'''


sort1 = group6.reset_index().sort_values(by = 'max')
print(sort1)
#       country                   province  max
# 291  Portugal                 Table wine   81
# 103   Croatia  Middle and South Dalmatia   82
# ..        ...                        ...  ...
# 118    France                   Bordeaux  100
# 227     Italy                    Tuscany  100


#sắp xếp tăng dần số chuỗi description  của description  theo country và province
group7 = reviews.groupby(['country', 'province'])['description'].agg([len, max])
sort2 = group7.reset_index().sort_values(by = ['len', 'max'], ascending= False)
#sắp xếp giảm dần thì thêm tham số ascending = false
#in ra chuỗi dài nhất của mỗi group và số chuỗi của mỗi group 
print(sort2)
#     country               province    len
# 179  Greece  Muscat of Kefallonian      1
# 192  Greece          Sterea Ellada      1
# ..      ...                    ...    ...
# 415      US             Washington   8639
# 392      US             California  36247

#tương tự là method sort_index 
