import pandas as pd

import numpy as np

import csv

df = pd.read_csv("/data/training/blackfriday.csv",sep=",")

with open("/data/training/testcaseprobability.txt", "r") as fd:

    lines = fd.read().splitlines()
only_male=df[df['Gender']=='M']

probability_male=len(only_male)/len(df)

only_female=df[df['Gender']=='F']

probability_female=len(only_female)/len(df)

q = (len(lines)+1)//2
for i in range(1,q):

    with open('/code/output/output{}.csv'.format(i), 'w') as out:

        writer = csv.writer(out, delimiter=",",lineterminator="\n")

        All_par_Age=df[df.Age==lines[2*i-1]]

        probability_All_par_Age_male=len(All_par_Age[All_par_Age.Gender=='M'])/len(only_male)

        probability_All_par_Age_female=len(All_par_Age[All_par_Age.Gender=='F'])/len(only_female)

        p = (probability_All_par_Age_male*probability_male)/((probability_male*probability_All_par_Age_male)+(probability_All_par_Age_female*probability_female))

        if (p>0.5):

            writer.writerow(['Male'])

        else:

            writer.writerow(['Female'])

        p_cat=df[df['City_Category']==lines[2*i]]

        p2=len(p_cat)/len(df)

        writer.writerow([str(round(p2,4))])