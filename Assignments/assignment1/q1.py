import pandas as pd
cols = ["Sno", "Department", "Branch", "Semester", "Course", "RegistrationNo", "StudentName", "Date", "Slot group", "Time", "ClassConducted", "ClassAttended"]
df = pd.read_csv("/data/training/SECTION1.csv",header=None, names=cols)
#data = pd.read_csv("/data/training/SECTION1.csv")
reg = df.RegistrationNo.unique()
name = df.StudentName.unique()
df_new = df.iloc[:,[5,6,7,11]]
df_new1  = pd.DataFrame({'RegistrationNo': reg,'Name': name})
a = df_new.groupby(["RegistrationNo","StudentName"])
d = pd.DataFrame([])
for i in range(64):
    b1 = a.get_group((reg[i],name[i]))
    c1 = b1.loc[:,['Date','ClassAttended']]
    e = c1.groupby("Date").sum().T
    d = d.append(e,ignore_index=True,sort=False)
result = pd.concat([df_new1, d], axis=1,sort=False)
with open("/data/training/testcase.txt", "r") as fd:
    lines = fd.read().splitlines()
q = (len(lines)+1)//2
for i in range(1,q):
    with open('/code/output{}.txt'.format(i), 'w') as output:
        output.write(lines[2*i-1])
        for j in range(64):
            if (reg[j]==lines[2*i-1]):
                a= result.loc[j,lines[2*i]]
                print("",file=output)
                print(int(a), file=output,end="")
