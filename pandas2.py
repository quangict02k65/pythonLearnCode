#INDEXING, SELECTING AND ASSIGNING IN PANDAS

import pandas as pd

reviews  = pd.read_csv(r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\winemag-data-130k-v2.csv", index_col= 0 )
option1 = pd.set_option('max_rows', 5)
print(reviews)
#review là một dataframe , coi nó như một đối tượng, do đó các tên cột cũng như là property của đối tượng
#do đó để gọi đến các cột trong dataframe ta sử dụng cách sau 
print(reviews.columns)
counTry = reviews.country
print(counTry)
#cách khác : bạn có thể truy cập vào nó qua toán tử indexing []
counTry2 = reviews['country']
print(counTry2)
#cách sử dụng index dễ dàng hơn và hữu ích hơn
#ví thử trong trường hợp tên cột của ta là 'country providence' thì chỉ indexing sử dung được 
#ta trông reviews khá giống như mảng hai chiều, vì thế để gọi đến tên quốc gia đầu tiên ta chỉ cẩn
conTry_first = reviews['country'][0]
print("ten quoc gia dau tien trong column là : ", conTry_first)

#pandas has its own accestor operator is loc and iloc
#iloc select toàn bộ một hàng dựa trên indexing nó truyền vào
row1 = reviews.iloc[1][2]
print(row1)
#iloc và loc đều là indexing truyền vào theo kiểu hàng trước, cột sau( trái ngược với python thông thường)

row2 = reviews.iloc[:, 0] #lấy tất cả các hàng, với cột = 0
print(row2)
# 0            Italy
# 1         Portugal
#             ...
# 129969      France
# 129970      France
row3 = reviews.iloc[:3, 0]
print(row3)

row4 = reviews.iloc[[3,4,5], 0]
print(row4)
# 3       US
# 4       US
# 5    Spain

#KIỂU LOC : LABEL-BASED SELECTION 
position1 = reviews.loc[0, 'country']
print(position1) #Italy

position2 = reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]
#lấy ra tất cả các hàng có cột tên là 3 cột như trên
print(position2)

'''
===>>> khi nào lấy ra dữ liệu mà chỉ có index truyền vào thì sử dụng iloc
===>>> khi nào lấy ra dữ liệu mà biết rõ tên column thì sử dụng loc
'''



#MANIPULATING THE INDEX
pri = reviews.set_index('title')
print(pri)
#kiểu là setup lại tập dữ liệu hữu ích hơn, khi mà title là cái quan trọng nhất thì mình đưa nó lên 
#cột đầu tiên của dataset

#CONDITIONAL SELECTION(lựa chọn có điều kiện)
#ví dụ như ta tìm thông tin của của các hàng có country là italy

italy = reviews.loc[reviews['country'] == 'Italy']
print(italy)

italy_90 = reviews.loc[(reviews['country'] == 'Italy') & (reviews['points'] >= 90) ] 
print(italy_90.loc[:, ['country', 'price']])#in ra country và price của các hàng thỏa mãn hai điểu kiện ở trên
#        country  price
# 120      Italy   70.0
# 130      Italy   70.0
# ...        ...    ...
# 129961   Italy   30.0
# 129962   Italy   40.0
#trong điều kiện này ta sử dụng toán tử : &(and) và |(or)

#pandas cũng có những built-in conditional selectors 
#isin: bạn chọn những dữ liệu mà có giá trị nằm trong list cho sẵn
isin1 = reviews.loc[reviews['country'].isin(['Italy', 'France'])]
print(isin1)
#        country                                        description  ...         variety                winery
# 0        Italy  Aromas include tropical fruit, broom, brimston...  ...     White Blend               Nicosia
# 6        Italy  Here's a bright, informal red that opens with ...  ...        Frappato       Terre di Giurfo
# ...        ...                                                ...  ...             ...                   ...
# 129969  France  A dry style of Pinot Gris, this is crisp with ...  ...      Pinot Gris  Domaine Marcel Deiss
# 129970  France  Big, rich and off-dry, this is powered by inte...  ...  Gewürztraminer      Domaine Schoffit

#the second is "isnull" và "notnull"
isnull1 = reviews.loc[reviews['price'].isnull()]
print(isnull1.loc[:, 'price'])


#ASSIGNING DATA
#EXAMPLE
reviews['critics'] = 'quang nguyen'
print(reviews.loc[:, ['critics', 'price']])

reviews['index_backwards'] = range(len(reviews), 0 , -1)
print(reviews['index_backwards'])
