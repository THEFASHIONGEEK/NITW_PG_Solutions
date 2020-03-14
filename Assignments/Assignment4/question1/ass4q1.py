import pandas as pd

import numpy as np

import csv

from scipy import stats

iq_data=np.loadtxt("/data/training/iqdata.csv")

iq1 = iq_data[0:10000]

f = open("/data/training/testcaseiq.txt")

nooftestcases = f.readline().strip()

for i in range(1,int(nooftestcases)+1):

    with open("/code/output/output{}.csv".format(i), "w") as out:

        writer = csv.writer(out, delimiter=",")

        writer.writerow([str(round(np.mean(iq1),2))])

        writer.writerow([str(round(np.std(iq1),2))])

        lb = f.readline().strip()

        ub = f.readline().strip()

        p = np.subtract(stats.norm(np.mean(iq1),np.std(iq1)).cdf(int(ub)), stats.norm(np.mean(iq1),np.std(iq1)).cdf(int(lb)))*100

        writer.writerow([str(np.round(p,3))])
        file = f.readline().strip()

        sample = pd.read_csv("/data/training/{}.csv".format(file))

        a = stats.ttest_1samp(a=sample,popmean=np.mean(iq1))

        if a[1][0] < 0.05:

            writer.writerow(["Reject"])

        else:

            writer.writerow(["Accept"])