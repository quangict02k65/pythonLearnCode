#học về kiểu dữ liệu string trong python 
#nháy đơn 
#' '
#nháy kép " "  
#trong hai cặp nháy trên là để biểu thị chuỗi trong python 
#trong chuỗi có dấu nháy đơn thì ta sử dụng dấu nháy kép để bao chuỗi lại 
#trong chuỗi có dấy nháy kép thì ta sử dụng dấu nháy đơn đẻ bao chuỗi lại

str_str = "I'm nguyen quang"
print(str)
print(type(str))

#chuỗi nhiều dòng với dấu '''  hoặc  dấu """
str_1 = '''nguyen ngoc quang
20205167
dai hoc bach khoa ha noi  '''
print(str_1)

# một số kí tự / đặc biệt 
'''
\t \n
\' \"  \\ => \
'''

#python cho phép chúng ta tạo nên một chuỗi trần , không có kí tự đặc  biệt trong nó 
str_special = r'nguyen ngoc "quanng " -- \\\ dsfj '
print(str_special)

#toán tử trong chuỗi 
#toán tử +
str_a = "nguyen "
str_b = "ngoc quang"
str_sum = str_a + str_b
print(str_sum)
#toán tử *
#tạo ra một chuỗi nhờ lặp đi lặp lại số lần chuỗi đã biết 
str_3 = 5 * str_a
print(str_3)
#toán tử in 
#kiểm tra xem một chuỗi có nằm bên trong chuỗi khác hay không 
#toán tử sẽ trả về true hoặc false 
print("ngu" in str_a)
str_end = str_a[len(str_a) - 1]
print(str_end)

#python cho phép chùng ra cắt chuỗi tương tự với list 
#chuỗi b là cắt từ chuỗi a lấy từ vị trí 1 đến 4
sub_str = str_b[:] #lấy cả chuỗi 
print(sub_str)
#có thẻ dùng cả bước nhảy 
sub_str1 = str_b[::-2] #bước nhảy âm nghĩa là đảo ngược lại chuỗi vừa cắt ra
print(sub_str1)

#ép kiểu dữ liệu 
str4 = "54545"
str5 = int(str4)
str6 = float(str4)
print(type(str4))
print(type(str5))
print(str6)
#ép kiểu từ số chuyển thành chuỗi 
str7 = 34324324
str8 = str(str7)
print(type(str7))


#python không cho sửa đổi nội dung chuỗi 
str_goc = "Quang nguyen ngoc" 
#ta muốn thay đổi kí tự o thành số 0
str_goc = str_goc[:-2] + "0" +str_goc[-1:]
print(str_goc)
