import numpy as np
import matplotlib.pyplot as pt
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

time_studied = np.array([18, 60, 80, 25, 63, 50, 10, 5, 8, 15, 70, 85]).reshape(-1,1)
scores = np.array([46, 70, 80, 50, 56, 60, 26, 10, 20, 15, 56, 95]).reshape(-1,1)

model = LinearRegression()
model.fit(time_studied, scores)

pt.scatter(time_studied, scores)
x = np.linspace(0,100,100).reshape(-1,1)
pt.plot(x, model.predict(x))
print(model.predict([[56]]))    # predict an specific value
pt.scatter([[56]], model.predict([[56]]))

# 
# we take time_train and score_train to do the linear regression, 
# and time_test and score_test to test the accurancy of the linear regression
# the test_size is the 20% of the total data (it will be the size of time_test and score_test)
# using the 80% for the linear regression
time_train, time_test, score_train, score_test = train_test_split(time_studied, scores, test_size=0.3)
model = LinearRegression()
model.fit(time_train, score_train)
value = model.score(time_test, score_test)
print(value)
fig = pt.figure()
pt.scatter(time_train, score_train)
x = np.linspace(0,100,100).reshape(-1,1)
pt.plot(x, model.predict(x))

pt.show()