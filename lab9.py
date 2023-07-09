import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
sales=np.array([2,4,6,9,12,34,45])
budgets=np.array([1,2,4,7,9,11,15])
x=budgets.reshape(-1,1)
y=sales
model=LinearRegression()
model.fit(x,y)
print("Coef:", model.coef_)
print("Intercept:", model.intercept_)
ypred=model.predict(x)
plt.scatter(x,y,color='b',label='actual sales')
plt.plot(x,ypred,color='r',label='linear regression')
plt.scatter(x,ypred,color='y',label='linear regression')
plt.xlabel("TV Budget")
plt.ylabel("Sales")
plt.legend()
plt.show()
