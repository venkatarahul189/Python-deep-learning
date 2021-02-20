import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read data from train.csv
train = pd.read_csv('train.csv')

#Display the scatter plot of GarageArea and SalePrice before deleting
plt.scatter(train.GarageArea, train.SalePrice, color='blue')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()

# calculate every range quarterly
print(train.GarageArea.describe())

#Deleting the outlier value of GarageArea
outlier_drop = train[(train.GarageArea >330) & (train.GarageArea <574)]

##Display the scatter plot of GarageArea and SalePrice after deleting
plt.scatter(outlier_drop.GarageArea, outlier_drop.SalePrice, color='pink')
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()