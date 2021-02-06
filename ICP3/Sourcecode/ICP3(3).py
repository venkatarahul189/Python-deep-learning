import numpy as np
#Create a random vector of size 20 by using randint
Z = np.random.randint(1, 20, 20)
print(Z)
#Reshaped the array to 4 by 5
x = Z.reshape((4,5))
print(x)
#Replace the max in each row by '0'
y = np.where(x == np.amax(x, axis=1, keepdims=True), 0, x)
print("Replace the max in each row by 0")
print(y)