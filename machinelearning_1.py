import pandas as pd

#luư file data dưới tên cho dễ gọi đến 
melbourne_file_path = r'C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\melb_data.csv'

#đọc dữ liệu từ file 
melbourne_data = pd.read_csv(melbourne_file_path) 

#loaị bỏ đi một số cột thiếu giá trị trong tập dữ liệu
filtered_melbourne_data = melbourne_data.dropna(axis = 0)
#in ra các cột thông tin trong file dữ liệu
print(melbourne_data.columns)
#your first machine learning model in kaggle platform 

y = filtered_melbourne_data.Price
print(y)

#lấy ra một số features nổi bật trong tập dữ liệu của chúng ta
#bằng cách chọn ra một số  cột của tập dữ liệu
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = filtered_melbourne_data[melbourne_features]

print(X.describe())#in toàn bộ ra màn hình 
print(X.head())#5 hàng đâu tiên 
print(X.tail())#5 hàng cuối cùng
print(X.median())#giá trị trung bình 

#next, we will use the scikit learn library to create our models
'''
the steps to building and using a model are : 
Define: what type of model will it be? a decision tree? some other type of model?
Some other parameters of the model type are specified too?
Fit: capture patterns from provided data. This is the heart of modeling( nắm bắt các mẫu từ dữ liệu)
Predict: Just what sounds like
Evaluate: Determine how accurate the model's predictions are
'''

#example
from sklearn.tree import DecisionTreeRegressor
#Define model. Specify a number for random_state to ensure same results each run 
melbourne_model = DecisionTreeRegressor(random_state=1)

#fit model
melbourne_model.fit(X,y)
print("making predictions for the following 5 houses: ")
print(X.head())
print("THe predictions are")
print(melbourne_model.predict(X.head()))

#model validation 
'''
ví dụ như màu sơn không liên quan tới giá của một căn nhà
tuy nhiên trogn tập dữ liệu của chúng ta thì đa số nhà có màu sơn xanh lại có giá cao
do đó mà mô hình của chúng ra đưa ra dự đoán nhà màu xanh có giá cao hơn những nhà khác
do đó sinh ra model validation 
model validation loại bỏ đi các dữ liệu không liên quan đế dự đoán của chúng ta.
'''
#we will learn to use model validation to measure the quality of your model
# there are many metrics for summarizing model quality , but we will start with one called
#Mean absolute Error(MAE)
from sklearn.metrics import mean_absolute_error
predicted_homes_prices = melbourne_model.predict(X)
print("sai so tuyet doi trung binh  cua mo hinh la :")
print(mean_absolute_error(y, predicted_homes_prices))

#data validation là data mà sau khi lược bỏ một số dữ liệu không chính xác, k xác thực
#tạo ra dự đoán tốt hơn cho model của mình 
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

#overfitting :ví dụ trong mô hình cây quyết định, khi chúng ta chia  ra nhiều nhánh quá 
#có thể dẫn tới dự đoán rất gần với kết quả trong tập huấn luyện của mình , tuy nhiên 
#nó không đưa ra dự đoán chính xác vs tập dữ liệu mới cần dự đoán
#underfitting là chia ra ít quá, thậm chí nó còn không hoạt động tốt với tập dữ liệu huấn luyện
#random forest là tạo ra rừng gồm nhiều cây và lấy trung bình giá trị của các cây, tạo thành 1 rừng
