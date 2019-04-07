import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('Health_Data_Set.csv')
X = df.iloc[:, 3].values
y = df.iloc[:, 4].values

plt.scatter(df['Diseases Name'],df['Deaths'])
plt.scatter(df['State'],df['Age-adjusted Death Rate'])

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)"""

# Feature Scaling
from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(X_train,y_train)
clf.predict(X_test)
y_test
clf.score(X_test,y_test)
    
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
State = df.iloc[:25, 2]
Deaths = df.iloc[:25, 3]
labels = State
sizes = Deaths
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()