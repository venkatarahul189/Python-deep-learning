import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder
#This is the imported data set
dataset = pd.read_csv('Breas Cancer.csv')
dataset.info()
#This is the dataset1 taken
x = dataset1 = dataset.iloc[:, [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31]]

le = LabelEncoder()
dataset['enc_diagnosis'] = le.fit_transform(dataset['diagnosis'].astype('str'))
y = dataset['enc_diagnosis']

X_train, X_test, Y_train, Y_test = train_test_split(x, y,
                                                    test_size=0.28, random_state=84)
np.random.seed(155)
# Here i create model
my_first_nn = Sequential() 
# i used hidden layer
my_first_nn.add(Dense(50, input_dim=29, activation='relu')) 
# This is the output layer
my_first_nn.add(Dense(1, activation='sigmoid')) 

my_first_nn.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,verbose=0,
                                     initial_epoch=0)
#This is the final output i printed here
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test,verbose=0))
