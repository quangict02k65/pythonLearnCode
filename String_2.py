#string 2 trong python 

#định dạng chuỗi trong python 
#định dạng bằng toán tử %
name = "My name is %s"%('Quang kubo')
print(name)
age = "My age is %d years old" %(19)
print(age)
score = "your sore is %.2f" %(12.4342)
print(score)
#===> giống hệt với lập trình c

#tác dụng của chữ f trong một chuỗi 
#nó gọi đến giá trị của biến trong dấu ngoặc nhọn
ten = "quang "
result = f"{ten} - nguyen ngoc quang "
print(result)

Name = "Nguyen Ngoc Quang "
Age = 19
Address = "KHu 16 Lam Thao Phu THo"
infor = f'''student: {Name}
age : {Age}
address: {Address}'''
print(infor)
# student: Nguyen Ngoc Quang
# age : 19
# address: KHu 16 Lam Thao Phu THo
#cách để clean code khi mà chưa biết thông tin là 
infor2 = f"name : {{Name}}"
print(infor2)
# name : {Name}
 # tạm thời để là name chưa điền


 #định dạng bằng phương thức format
dinhDang = "a: {2}, b: {0}, c:{1}".format(1,2,3)
print(dinhDang)
#khi ta thêm chỉ số vào dấu ngoặc nhọn thì nó sẽ lấy theo thứ tự trong ngoặc nhọn
inRa = "%-7s%-10d" %("quang", 19)
print(inRa)

#string method
#method capitalize
s1 = "ngyDSHFSJKDH quang "
s2 = s1.capitalize() #trả lại một chuỗi in hoa chữ cái đầu tiên, các kí tự còn lại giữ nguyên
print(s1)
print(s2)

#method uppper
s3 = s1.upper()
print(s3)
s4 = s1.lower()
print(s4)

#method swapcase
#chữ thường thành chữ hoa và chữ hoa thành chữ thường
s5 = s1.swapcase()
print(s5)

#method title
string1 = "nguyễn quang"
string2 = string1.title() #kiểu chuẩn hóa chuỗi chưa bỏ khoảng trắng
print(string2)

#method center
#căn giữa lề, cái điền vào là cái hiển thị ra màn hình 
# -------------------------------------------nguyen  quang--------------------------------------------     
string3 = string1.center(100, "-") #fillchar chỉ là chuỗi có độ dài là 1.
print(string3)
#căn trái là ljust
#căn phải là rjust

#phương thức encode
#là phương thức để mã hóa một chuỗi
string4 = string1.encode(encoding = 'utf-8', errors = 'strict')
print(string4)

string5 = string1.join(['1', '2', '3'])
print(string5)#đan xen chuỗi 
# 1nguyễn quang2nguyễn quang3

#method replace
#thay thế chữ cái gì đó trong chuỗi ban đầu bằng kí tự mới 
string6 = string1.replace('n', 'dị', 1) #thêm count vào là số kí tự thay thế
print(string6)

#method strip
#cắt chữ nào đó ở hai đầu đi 
#ngoài ra còn có rstrip và lstrip
string7 = string1.strip("ng")
print(string7)

Str1 = "   nguyen quang    "
Str2 = Str1.strip()
print("chuoi ban dau la [%s]"%(Str1))
print("chuoi sau do la [%s]"%(Str2))

#method split
#đưa chuỗi ban đầu thành một list được cắt ra bởi tham số đưa vào 
chuoi1 = "nguyen ngoc quang"
chuoi2 = chuoi1.split(" ", 2)#tham số đằng sau nghĩa là cắt bao nhiêu lần 
print(chuoi2)
#rsplit cắt từ phía bên phải qua


#method partition 
chuoi3 = chuoi1.partition('n')
#ra 3 phần tử là phần trước chữ nguyen, chu nguyuen và phần sau chữ nguyen 
# ('', 'n', 'guyen ngoc quang')
#rpartition là cắt từ phía bên phải qua trái 
print(chuoi3)

#phương thức count
cnt = chuoi1.count('nguyen',0,4)
#tham số phía sau là start và end 
print(cnt)

#method startwith
#trả về true nếu bắt đầu bằng kí tự nào đó, ngược lại thì trả về false
result = chuoi1.startswith('n',5,10)
#tham số phía sau là bắt đầu và kếu thúc ở kí tự thứ mấy
print(result)


#method end
result2 = chuoi1.endswith('g')
print(result2)

#method find
#trả về vị trí đầu tiên tìm thấy kí tự trong ngoặc
result3 = chuoi1.find("j")
print(result3)
#method rfind(tìm từ bên phải )


#method index
result4 = chuoi1.index('n')
print(result4)
#khác nhauu giữa index và find là  find  nếu không tìm thấy thì quăng ra -1
#còn index nếu không tìm thấy thì lỗi biên dịch
#rindex là tìm từ bên phải và quăng ra vị trí tìm thấy đầu tiên 

#method islower
#method isupper
#method isalpha
#method isdigit
#method isspace








