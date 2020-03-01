import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
import warnings 
warnings.filterwarnings("ignore")
#import data
df = pd.read_csv('/data/training/Data.csv')
#Create a Bayesian Model by defining the edges of the network
model = BayesianModel([('asia','tub'),('smoke','lung'),('smoke','bronc'),('tub','either'),('either','xray'),('bronc','dysp'),('lung','either'),('either','dysp')])
#Cross check if the nodes and edges added are reflected in the model correctly.
print("Nodes:", model.nodes(), end="\n")
print("Edges:", model.edges(), end="\n")
#Define Conditional Probability Distributions for all the nodes of the model.
estimator = MaximumLikelihoodEstimator(model,df)
cpds = estimator.get_parameters()
#Add the CPD’s to model and cross check the CPD’s 
for i in range(0,8):
    model.add_cpds(cpds[i])
#Check the consistency of Model
print(model.check_model())
#Graphical representation of the model 
import matplotlib.pyplot as plt
import networkx as nx
nx.draw_shell(model,with_labels=True)
plt.show()
#Create Inference Object of the model 
model_inference = VariableElimination(model)
#query
query1 = model_inference.map_query(variables=['tub'], evidence={'smoke':1, 'dysp':0})
query2 = model_inference.map_query(variables=['xray'], evidence={'lung':1, 'asia':1})
query3 = model_inference.query(variables=['bronc'],evidence={'asia':1, 'dysp':1,'either':0})
#convert dictionary to list
q1 = [[ k,v ]for k, v in query1.items()]
q2 = [[k, v] for k, v in query2.items()]
q3 = [[k, v] for k, v in query3.items()]
data = {"Query1":q1[0],"Query2":q2[0],"Query3":q3[0]}
result = pd.DataFrame(data) 
result.to_csv('/code/output/output.csv', index=False)





