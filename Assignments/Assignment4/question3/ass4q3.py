from sklearn import datasets

import numpy as np

import csv

import warnings

warnings.filterwarnings("ignore")

iris = datasets.load_iris()

x = iris.data

y = iris.target

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import cross_val_score

clf = LogisticRegression()

scores = cross_val_score(clf, iris.data, iris.target, cv=5,scoring="accuracy")

with open("/code/output/output.csv", "w") as out:

    writer = csv.writer(out, delimiter=",")

    writer.writerow([str(round(np.mean(scores),4))])