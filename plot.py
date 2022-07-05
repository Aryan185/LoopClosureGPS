import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Dataset.csv')

X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values

"""plt.scatter(X, y, color = 'cyan')
plt.title('Error wala graph')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()"""

def dist(x1,y1,x2,y2):
    del_x = x2-x1
    del_y = y2-y1
    del_x_sq = np.square(del_x)
    del_y_sq = np.square(del_y)
    sq_sum = del_x_sq + del_y_sq

    dist = np.sqrt(sq_sum)

    return dist

for i in range(1,571):
    dist_from_origin = dist(int(X[0]),int(y[0]),int(X[i]),int(y[i]))

    if X[i]==X[0]:
        X[i+1]=0
        y[i+1]=0
        for k in range(i-15, i):
            X[k] = X[k]/1.1
            y[k] = y[k]/1.1


plt.scatter(X, y, color='red', s=10)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()