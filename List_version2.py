#list phần 2

#phương thức count 
a = [1,2,3,4,5,6,7,4,2,2,2,2]
c = a.count(2)
print("so lan xuat hien cua so 2 la ", c)

#phương thức index
c_1 = a.index(2) #lần xuất hiện đầu tiên của số 2 trong list
print(c_1)

#phương thức copy
c_2 = a.copy() #tạo ra bản sao và không trỏ về một nơi.
print(c_2)

#phương thức clear
# c_3 = a.clear()
# print(c_3) # ra none 
# print(a)

#phương thức append
print(a)
a.append([3,4]) #thêm từng phần tử một
print(a)

#phương thức extend
a.extend([4,5,6,[3,4,5,5]]) #có thể thêm nhiều phần tử cùng một lúc .
print(a)
# [1, 2, 3, 4, 5, 6, 7, 4, 2, 2, 2, 2, [3, 4], 4, 5, 6, [3, 4, 5, 5]]

#phương thức insert
a.insert(0,[3,4,5]) #thêm phần tử [3,4,5] vào vị trí thứ 0
print(a)

#phương thức pop
c_5 = a.pop(1)#lấy ra list bỏ đi phần tử a[1] trong list
#nếu không có số 1 truyền vào thì mặc định là bỏ đi phần tử cuối cùng trong list
print(a)
print(c_5)

#Phương thức remove
a.remove(2) #xóa di phần tử 2 đầu tiên ở trong list
print(a)#nếu không có trong list thì sẽ bị lỗi

#phương thức reverse
a.reverse() #đảo ngược lại list
print(a)

#phương thức sort
b = [2,3,4,5,6,2,1,4]
b.sort(reverse = True) #mặc định là sắp xếp nhỏ tới lớn
print(b)#khi ta truyền tham số reverse = true vào thì nó sẽ đảo ngược lại
#thành sắp xếp từ lớn tới bé

