import pandas as pd
q1 = pd.read_csv("/data/training/quiz/quiz1.csv")
q1_new = q1.iloc[0:659,[1,10]]
q1_new.columns = ['studentName','grade']
q2 = pd.read_csv("/data/training/quiz/quiz2.csv")
q2_new = q2.iloc[0:680,[1,10]]
q2_new.columns = ['studentName','grade']
data = pd.read_csv("/data/training/studentlist.csv")
dict_of_df = {} # initialize empty dictionary
for i in range(1,20):
    b1 = pd.read_csv('/data/training/batchwiselist/{}.csv'.format(i))
    s0 = pd.merge(b1.iloc[:,[1,4]], q1_new, how='left', on=['studentName'])
    s1 = pd.merge(b1.iloc[:,[1,4]], q2_new, how='left', on=['studentName'])
    list = {"s0":s0,"s1":s1}
    df = pd.DataFrame(columns=["noofpresent", "lessthan50", "between50and60", "between60and70", "between70and80", "greaterthan80"])
    for j in range(2):
        a = list["s{}".format(j)]
        l = []
        l.append(len(a.loc[(a['grade'] <='9.0') ]))
        l.append(len(a.loc[(a['grade'] != '10.0')&(a['grade'] <='5.0') ]))
        l.append(len(a.loc[(a['grade'] =='6.0') ]))
        l.append(len(a.loc[(a['grade'] =='7.0') ]))
        l.append(len(a.loc[(a['grade'] =='8.0')]))
        l.append(len(a.loc[(a['grade'] =='9.0') ])+len(a.loc[(a['grade'] =='10.0') ]))
        df.loc[j] = l
    dict_of_df["df_{}".format(i)] = df
with open("/data/training/testcaseStudent.txt", "r") as fd:
    lines = fd.read().splitlines()
p = (len(lines)+1)//2
for i in range(1,p):
    with open('/code/output{}.txt'.format(i), 'w') as output:
        for j in range(1,20):
            if ("{}.csv".format(j)==lines[2*i-1]):
                a = dict_of_df["df_{}".format(j)]
                b = a.loc[0,lines[2*i]]
                c = a.loc[1,lines[2*i]]
                #print(" ",file=output,end='')
                print(int(b), file=output)
                #print("",file=output,end='')
                print(int(c), file=output,end="")
