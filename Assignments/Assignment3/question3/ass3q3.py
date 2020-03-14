import pandas as pd

import numpy as np

import csv

df = pd.read_csv("/data/training/blackfriday.csv",sep=",")

b = []

b.append([np.round(df["Purchase"].var(),2)])

b.append([np.round(df["Purchase"].std(),2)])

from scipy.stats import skew

b.append([np.round(skew(df["Purchase"]),2)])

from scipy.stats import kurtosis
b.append([np.round(kurtosis(df["Purchase"]),1)])

with open("/code/output/output.csv", "w") as out:

    writer = csv.writer(out, delimiter=",")

    for i in range(0,len(b)):

        writer.writerow(b[i])