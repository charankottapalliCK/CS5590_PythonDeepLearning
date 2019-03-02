import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

train = pd.read_csv('weatherHistory.csv')

#Working with Numeric Features
numeric_features = train.select_dtypes(include=[np.number])

corr = numeric_features.corr()

print (corr['Temperature (C)'].sort_values(ascending=False)[:5], '\n')
print (corr['Temperature (C)'].sort_values(ascending=False)[-5:])

quality_pivot = train.pivot_table(index='Humidity',
                                  values='Temperature (C)', aggfunc=np.median)
print(quality_pivot)

#Notice that the median sales price strictly increases as Overall Quality increases.
quality_pivot.plot(kind='bar', color='blue')
plt.xlabel('Overall Quality')
plt.ylabel('Median Sale Price')
plt.xticks(rotation=0)
plt.show()

##Null values
nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

##handling missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()
print(sum(data.isnull().sum() != 0))

##Build a linear model
y = train['Temperature (C)']
X = pd.get_dummies(train)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, random_state=42, test_size=.33)
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
##Evaluate the performance and visualize results
print ("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

##visualize

actual_values = y_test
plt.scatter(predictions, actual_values, alpha=.75,
            color='b') #alpha helps to show overlapping data
plt.xlabel('Temparature')
plt.ylabel('All values')
plt.title('Linear Regression Model')
plt.show()
