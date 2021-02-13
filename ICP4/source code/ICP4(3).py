import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

glass = pd.read_csv('glass.csv')
x = glass[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']]
y = glass['Type']
# Use train_test_split to create training and testing part
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
SVM = LinearSVC(random_state=0)
SVM.fit(x_train, y_train)
print('Accuracy of SVM classifier on test set:', round(SVM.score(x_test, y_test) * 130, 2))
