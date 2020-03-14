# Import libraries here
import numpy as np
from sklearn import linear_model
import csv
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# [Example] Read datasets
cars = pd.read_csv("/data/training/mtcars.csv")

# User can save any number of plots to `/code/output` directory
# Note that only the plots saved in /code/output will be visible to you
# So make sure you save each plot as shown below
# Uncomment the below 3 lines and give it a try
# axes = pd.tools.plotting.scatter_matrix(iris_train, alpha=0.2)
# plt.tight_layout()
# plt.savefig('/code/output/scatter_matrix.png')

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge, Lasso

X = cars.drop(['model', 'mpg'], axis=1)
y = cars['mpg']

lasso = Lasso(alpha=1.0)
ridge = Ridge(alpha=1.0)

lasso.fit(X, y)
ridge.fit(X, y)

#K fold cross validation
num_folds = 10
seed = 42
#kfold = KFold(n_splits=num_folds, random_state=seed)
cv_lasso = cross_val_score(lasso, X, y, cv = num_folds)
cv_ridge = cross_val_score(ridge, X, y, cv = num_folds)

mean_diff = np.round((np.mean(cv_ridge) - np.mean(cv_lasso)), 2)
print(mean_diff)

# Write output file
out = open('/code/output/output.csv', 'w')
writer = csv.writer(out, delimiter = ',')
writer.writerow([str(mean_diff)])
out.close()