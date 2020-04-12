import numpy as np
import pandas as pd
import csv
from scipy.stats import mode
df = pd.read_csv("/data/training/autompg.csv")
m = df["mpg"].mean()
sd = df["mpg"].std()
from scipy.stats import pearsonr
a = pearsonr(df["weight"],df["mpg"])
gh = mode(df["mpg"])
with open("/code/output/output.csv", "w",newline='') as out:
    writer = csv.writer(out, delimiter=",")
    writer.writerow([str(np.round(m,2))])
    writer.writerow([str(int(df["mpg"].median()))])
    writer.writerow([str([gh[0][0]])])
    writer.writerow([str(np.round(sd,2))])
    writer.writerow([str(np.round(df["weight"].corr(df["mpg"],method ='kendall'),2))])
    writer.writerow([str(np.round(a[0],2))])
f = open("/data/training/testcaseauto.txt")
nooftestcases = f.readline().strip()
for i in range(1,int(nooftestcases)+1):
    lb = f.readline().strip()
    df1=pd.read_csv("/data/training/{}.csv".format(lb))
    m1 = df1["mpg"].mean()
    sd1 =df1["mpg"].std()
    with open("/code/output/output{}.csv".format(i), "w",newline='') as out:
        writer = csv.writer(out, delimiter=",")
        writer.writerow([str(np.round(m-m1,2))])
        writer.writerow([str(np.round(sd-sd1,2))])
