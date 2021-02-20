import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the data
dframe = pd.read_csv('data.csv')
convert = {"City Group": {"Big Cities": 0, "Other": 1}, "Type" : {"FC" : 0, "IL" : 1, "DT" : 2}}
data = dframe.replace(convert)

#check the data types
data.revenue.describe()
y = np.log(data.revenue)
x = data.drop(['revenue', 'Id'], axis=1)

#train test split imported
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=40, test_size=.33)
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(x_train, y_train)

#Evaluate the model using RMSE and R2 score.
print ("R squared error : \n", model.score(x_test, y_test))
predictions = model.predict(x_test)
from sklearn.metrics import mean_squared_error
print ('RMSE error : \n', mean_squared_error(y_test, predictions))

#prediction plot of the data
plt.scatter(predictions, y_test, alpha=.65,color='g')
plt.title('Linear Regression Model')
plt.xlabel('actual price')
plt.ylabel('predicted Price')
plt.show()