import pandas as pd
import numpy as np
import csv


"""
I.Load 1000 rows from the dataset from the file bottle.csv.
"""

df_all = pd.read_csv("/data/training/bottle.csv", nrows=1000)
df = df_all[['Salnty','T_degC']]


# Write your code here
#Replace null values with their respective mean
df['Salnty'] = df['Salnty'].fillna(df['Salnty'].mean())
df['T_degC'] = df['T_degC'].fillna(df['T_degC'].mean())

from sklearn.model_selection import train_test_split
X = df['Salnty']
y = df['T_degC']

seed = 42
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = seed)
print('x_train',x_train.shape, '\ny_train',y_train.shape, '\nx_test',x_test.shape,'\ny_test', y_test.shape)

x_train = x_train.values.reshape(-1, 1)
x_test = x_test.values.reshape(-1, 1)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(x_train, y_train)
print('Model coefficient :', lm.coef_, '\nModel intercept :', lm.intercept_)
intercept = [np.round(lm.intercept_, 3)]
coefficient = [np.round(lm.coef_, 3).tolist()]
print(intercept, coefficient)

#prediction
y_pred = lm.predict(x_test)

#Mean squared error and R square
from sklearn.metrics import mean_squared_error, r2_score
print('Mean squared error', mean_squared_error(y_test, y_pred))
print('Variance score ', r2_score(y_test, y_pred))
MSE = np.round(mean_squared_error(y_test, y_pred), 3)
R2 = np.round(r2_score(y_test, y_pred), 3)
print("MSE", MSE)
print('R square', R2)

#Perform 5 fold cross validation
from sklearn.model_selection import KFold, cross_val_score
num_folds = 5
kfold = KFold(n_splits = 5, random_state=seed)
cv_results = cross_val_score(lm, x_train, y_train, cv=kfold, scoring = 'neg_mean_squared_error')
neg_MSE = cv_results.tolist()
RMSE = [np.sqrt(np.abs(x)) for x in neg_MSE]
#print('cv_RMSE', RMSE)
mean_RMSE = np.round(np.mean(RMSE), 3)
print('Mean RMSE', mean_RMSE)

#print to output file 1
out1 = open('/code/output/output1.csv', 'w')
writer = csv.writer(out1, delimiter = ',')
writer.writerow([str(x_train.shape[0])])
writer.writerow([str(x_test.shape[0])])
writer.writerow([str(coefficient)])
writer.writerow([str(intercept)])
out1.close()

#print to output file 2
out2 = open('/code/output/output2.csv', 'w')
writer = csv.writer(out2, delimiter = ',')
writer.writerow([str(MSE)])
writer.writerow([str(R2)])
writer.writerow([str(mean_RMSE)])
out2.close()
