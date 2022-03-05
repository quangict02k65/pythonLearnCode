# pythonLearnCode
#List là một container được sử dụng rất nhiều trong python 
#một list được giới hạn bởi các cặp []
#List có khả năng chứa mọi kiểu giá trị , kể cả chính nó 

# list = [1, 3, "quang", 45.3]
# print(list)
# print(type(list))

# list_ = [[[1,2,3,4], [4,5,6]], ["quang", "quang n"]]
# print(list_)

# #List rỗng
# list_1 = []

# #tạo một list từ 0 đến 3
# a = [i for i in range(3)]
# print(a)

# #tạo list bằng công thức.
# list_2 = [[n, n*1*4, n*2] for n in range(1,4)]
# print(list_2)

#sử dụng constructor list 
list_3 = list([1,2,3])
list_4 = list("quang nguyen ")
print(list_3)
print(list_4)
# [1, 2, 3]
# ['q', 'u', 'a', 'n', 'g', ' ', 'n', 'g', 'u', 'y', 'e', 'n', ' ']
#iterable là một tập hợp nhiều phần  tử(truyền int vào k chạy được vì int không phải tập hợp nhiều phần tử)

#phép công list - cùng kiểu dữ liệu mới có các phép tính 
list_4 = [1,2]
list_4 += ["quang", 'nguyen ']
print(list_4)
# [1, 2, 'quang', 'nguyen ']

#phép nhân list với một số 
list_5 = [1,2 ]
list_5 *= 5;
print(list_5)
# [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

#kiểm tra một số có nằm trong list hay không
list_6 = ["quang", 4, 3]
b = "quang" in list_6
print(b)
#true

list_7 = [1,2, [1,3,4], 'quang', "nguyen "]
b = list_7[-1] #nguyen lấy phần tử cuối cùng của môt list
print(b)

#lấy ra một list con trong list
list_8 = [1,2,3, "quang", [1,3,4], [3,4,5], 3]
subList = list_8[1:6] #lấy ra từ phần tử a[1] đén phần tử a[5]
print(subList)
subList_2 = list_8[:5]#lấy từ phần tử đầu tiên tới phần tử a[4]
print(subList_2)
subList_3 = list_8[2:]#lấy từ phần tử a[2] đến phần tử cuối cùng
print(subList_3)
subList_4 = list_8[::-1]#lấy toàn bộ và đảo ngược lại
print(subList_4)
subList_5 = list_8[:-1]#bỏ lại thằng -1
print(subList_5)
subList_6 = list_8[::] #lấy hết phần tử trong list = list_8[:]
print(subList_6)

#thay đổi nội dung của list
list_9 = [1,2,'a','b']
list_9[1]= "quang"
print(list_9[1])

#ma trận ( list chứa trog list) hay là mảng hai chiều.
matrix = [[1,2,3], [4,5,6],[7,8,9]]
print(matrix[0])
print(matrix[1])
print(matrix[2][1])

#kiểu list là kiểu tham chiếu nên không gán list này cho list khác
#khi thay đổi list này là list khác cũng thay đổi
#khi gán list này cho list khác thì cả hai cùng trỏ vào một chỗ 
#=>>>> khi gán giá trị của list, phải copy giá trị của list
#ta dùng constructor list
ar_1 = [1,2,3]
ar_2 = list(ar_1)
ar_2[1] = "quang"
print(ar_1)
print(ar_2)
