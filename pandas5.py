#DATATYPES AND MISSING VALUES


'''in this tutorial , i will learn how to investigate data types within a Dataframes and series
i will also learn how to find and replace entries
'''

import pandas as pd


reviews  = pd.read_csv(r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\winemag-data-130k-v2.csv", index_col= 0 )
option1 = pd.set_option('max_rows', 5)

#use dtype property to grab the type of the column
type_price = reviews['price'].dtype
print(type_price)
#float64

type_country = reviews['country'].dtype
print(type_country)
#dtypes return the dtype of every column in the dataframe
all_dtype = reviews.dtypes
print(all_dtype)
# country        object
# description    object
#                 ...
# variety        object
# winery         object
# Length: 13, dtype: object

'''
One peculiarity(điểm đặc biệt) to keep in mind is that colums consisting entirely
of strings do not get their own type
they are instead given the object type
'''

print(reviews['points'].dtype)
#int64


print(reviews['points'].astype('float64').dtype) #float64
print(reviews['points'].astype('float64'))


#MISSING DATA
'''
to select NaN entries you can use pd.isnull() 

'''
print(reviews[pd.isnull(reviews['country'])])
#        country                                        description  ...    variety              winery
# 913        NaN  Amber in color, this wine has aromas of peach ...  ...    Chinuri  Gotsa Family Wines
# 3131       NaN  Soft, fruity and juicy, this is a pleasant, si...  ...  Red Blend   Barton & Guestier
# ...        ...                                                ...  ...        ...                 ...
# 129590     NaN  A blend of 60% Syrah, 30% Cabernet Sauvignon a...  ...  Red Blend           Büyülübağ
# 129900     NaN  This wine offers a delightful bouquet of black...  ...     Merlot              Psagot


'''
replaceing missing value is a common operation . pandas provides a really handy method for 
this problem: fillna() 
fillna() provides a few different strategies for mitigating such data(chiến lược khác nhau để giảm thiểu dữ liệu)
vì NnN mặc định là kiểu float64
'''

fillna = reviews['region_2'].fillna("unknown")
print(fillna)
print(fillna.dtype)

#phương thức thay đổi là replace()
replace1 = reviews['taster_twitter_handle'].replace("@kerinokeefe", "quangnguyen")
print(replace1)
#replace hữu dụng khi ví thử những dữ liệu NaN chúng ta để là
#"unknows", "undisclosed" hay "invalid" ...
