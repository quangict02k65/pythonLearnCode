#REAMAINING AND COMBINING


import pandas as pd


reviews  = pd.read_csv(r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\winemag-data-130k-v2.csv", index_col= 0 )
option1 = pd.set_option('max_rows', 5)

'''
the first function is rename()
'''
#rename tên cột
rename1 = reviews.rename(columns={'points':'score'})
print(rename1['score'])

#rename index
rename2 = reviews.rename(index = {0: 'first', 1: 'second'})
print(rename2)
#          country                                        description  ...         variety                winery
# first      Italy  Aromas include tropical fruit, broom, brimston...  ...     White Blend               Nicosia
# second  Portugal  This is ripe and fruity, a wine that is smooth...  ...  Portuguese Red   Quinta dos Avidagos
# ...          ...                                                ...  ...             ...                   ...
# 129969    France  A dry style of Pinot Gris, this is crisp with ...  ...      Pinot Gris  Domaine Marcel Deiss
# 129970    France  Big, rich and off-dry, this is powered by inte...  ...  Gewürztraminer      Domaine Schoffit



''' COMBINING '''
'''
pandas has three methods for doing combine different dataframes or series
'''
#concat()
#most of what merge() can do can also be done more simply with join()
'''
this is useful when we have data in different dataframe or series objects but having the same fields(colums)
'''
'''
canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")
pd.concat([canadian_youtube , british_youtube])
'''

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                        'key2': ['K0', 'K1', 'K0', 'K1'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
   

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                          'key2': ['K0', 'K0', 'K0', 'K0'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)

merge1 = pd.merge(left,right, on = ['key1', 'key2']) #on là tên cột hoặc index level để join(lưu ý là phải có ở cả 2 dataframes)
print("sau khi merge 1 la : \n", merge1) 


#how(mặc định là inner)
# Merge method	SQL Join Name	Description	_merge
# left	LEFT OUTER JOIN	Chỉ sử dụng keys của frame bên trái	left_only
# right	RIGHT OUTER JOIN	Chỉ sử dụng keys của frame bên phải	right_only
# outer	FULL OUTER JOIN	Sử dụng từng keys của 2 frames	both
# inner	INNER JOIN	Sử dụng keys giao nhau của 2 frames	both
merge2 = pd.merge(left, right, how = 'left', on = ['key1', 'key2'])
print("sau khi merge 2 la : \n",merge2)
#   key1 key2   A   B
# 0   K0   K0  A0  B0
# 1   K0   K1  A1  B1
# 2   K1   K0  A2  B2
# 3   K2   K1  A3  B3
#   key1 key2   C   D
# 0   K0   K0  C0  D0
# 1   K1   K0  C1  D1
# 2   K1   K0  C2  D2
# 3   K2   K0  C3  D3
# sau khi merge 1 la :
#    key1 key2   A   B   C   D
# 0   K0   K0  A0  B0  C0  D0
# 1   K1   K0  A2  B2  C1  D1
# 2   K1   K0  A2  B2  C2  D2
# sau khi merge 2 la :
#    key1 key2   A   B    C    D
# 0   K0   K0  A0  B0   C0   D0
# 1   K0   K1  A1  B1  NaN  NaN
# 2   K1   K0  A2  B2   C1   D1
# 3   K1   K0  A2  B2   C2   D2
# 4   K2   K1  A3  B3  NaN  NaN

merge3 = pd.merge(left, right, how='outer', on=['key1', 'key2'])
#   key1 key2    A    B    C    D
# 0   K0   K0   A0   B0   C0   D0
# 1   K0   K1   A1   B1  NaN  NaN
# 2   K1   K0   A2   B2   C1   D1
# 3   K1   K0   A2   B2   C2   D2
# 4   K2   K1   A3   B3  NaN  NaN
# 5   K2   K0  NaN  NaN   C3   D3

#tham số indicator

#truy cập đường link xem thêm .
# https://labs.flinters.vn/pandas/tim-hieu-pandas-bai-3-group-merge-du-lieu/

left1 = pd.DataFrame({'A' : [1,2,3], 'B' : [1,2,2]})
right1 = pd.DataFrame({'A' : [4,5,54], 'B': [1,2,5]}) 
result = pd.merge(left1, right1, on='B', how='inner', validate="many_to_one")
print(result)
