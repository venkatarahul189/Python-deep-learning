from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.model_selection import train_test_split
Glass = pd.read_csv('glass.csv')
x = Glass[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]
y = Glass['Type']
# Use train_test_split to create training and testing part
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
clf = GaussianNB()
clf.fit(x_train, y_train)
print('Accuracy of Naive Bayes GaussianNB on test set:', round(clf.score(x_test, y_test) * 150, 2))
