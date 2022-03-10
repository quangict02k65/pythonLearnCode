''' SCATTER PLOTS ( PHÂN TÁN DỮ LIỆU )'''
from cProfile import label
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# Path of the file to read
file = r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Desktop\data\insurance.csv"
insurance_data = pd.read_csv(file)

#to create simple scatter plot, we use the sns.scatterplot command and specify the values for : 
'''
1.the horizontal x-axis( x = insurance_data['bmi'])
2.the vertical y-axis ( y = insurance_data['charges'])
'''

sns.scatterplot(x = insurance_data['bmi'], y = insurance_data['charges'])


#vẽ regression line ( đường thẳng hồi quy )
#đường thẳng sao cho giá trị tổng bình phương các độ lệch khoảng cách theo phương thẳng đứng giữa các điểm và đường thẳng là nhỏ nhất
sns.regplot(x = insurance_data['bmi'], y = insurance_data['charges'])
#plt.show()


'''COLOR-CODED SCATTER PLOTS
For instance, to understand how smoking affects the relationship between BMI and insurance costs, 
we can color-code the points by 'smoker', and plot the other two columns ('bmi', 'charges') on the axes.'''

sns.scatterplot(x = insurance_data['bmi'], y = insurance_data['charges'], hue=insurance_data['smoker'])
# plt.show()

#thêm đường hồi quy cho người hút thuốc và người không hút thuốc
sns.lmplot(x = "bmi", y = "charges", hue = "smoker", data= insurance_data)
#plt.show()

#nhận thấy rằng với người hút thuốc thì càng nhiều cân thì số tiền trả càng lớn , đồ thị dốc 
#người không hút thuốc thì đồ thị hơi dốc nhẹ


#chúng ta có thẻ nhóm dữ liệu
#bằng command sns.swarmplot

'''ví dụ ta muốn nhóm trục x thành hai nhóm hút thuốc và không hút thuốc
và trục y là số tiền phải trả
'''
#swarm approximately group

sns.swarmplot(x = insurance_data['smoker'], y = insurance_data['charges'])
plt.show()

''' từ sự nhóm này lại ta thấy rằng những người hút thuốc dc tính phí cao hơn người không hút thuốc
người trả phí nhiều nhất là người hút thuốc
người trả phí thấp nhất là người không hút thuốc

'''
