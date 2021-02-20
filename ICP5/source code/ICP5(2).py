import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#here i imported the data
dframe = pd.read_csv('data.csv')

convert = {"City Group":{"Big Cities": 0, "Other": 1}, "Type" : {"FC" : 0, "IL" : 1, "DT" : 2}}
data = dframe.replace(convert)
y = np.log(data.revenue)
x = data.drop(['revenue', 'Id'], axis=1)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=.29)

#here i used the linear regression as 'lr'
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(x_train, y_train)

#Evaluate the model using RMSE and R2 score.
print ("R squared error : \n", model.score(x_test, y_test))
predictions = model.predict(x_test)
from sklearn.metrics import mean_squared_error
print('RMSE error : \n', mean_squared_error(y_test, predictions))

#This is for prediction plot of the data given
plt.scatter(predictions, y_test, alpha=.55,color='y')
plt.title('Multiple Regression Model')
plt.xlabel('actual price')
plt.ylabel('predicted price')
plt.show()