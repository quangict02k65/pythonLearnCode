# import math

# print("it is math! it has type", type(math))
# print(dir(math))

# #cách sử dụng hàm 
# help(math.isqrt)

# print(math.sqrt(34))

# #other import syntax
# import math as mt
# print(mt.pi)
# import pandas as pd
# import numpy as np

#cách khác giúp chúng ta không phải thay thế math.pi bằng pi

#lỗi khi dùng cách này là hàm log có cả ở trong hai hàm và chương trình sẽ hiểu là hàm log 
#sẽ overwrite lên hàm log của math
# from math import *
# from numpy import *
# print(pi, log(12,3))

#cách sử lý
from math import log, pi
from numpy import asanyarray
print(pi, log(112,3))
