import pandas as pd
#import libraries
from pgmpy.models import BayesianModel
from pgmpy.estimators import ParameterEstimator
b = [[0.25,0.33,0.17,1.0],[0.75,0.67,0.83,0.0]]
#load the dataset
data = pd.read_csv("/data/training/data1.csv", delimiter=" ")
model = BayesianModel([("fruit","tasty"),("size","tasty")])
est = ParameterEstimator(model,data)
a = est.state_counts
#Write your code below
fruit_counts = a("fruit")
size_counts = a("size")
tasty_counts = a("tasty")
#write you output to csv
tasty_counts.to_csv('/code/output/output1.csv')

#Question2

#create a Bayesian Model and generate CPD using MLE
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
estimator = MaximumLikelihoodEstimator(model,data)
cpds = estimator.get_parameters()
#Write your code
fruit_cpd = cpds[0]
size_cpd = cpds[1]
tasty_cpd = cpds[2]
print(tasty_cpd)
#write cpd of tasty to csv
res = pd.DataFrame(b)
res.to_csv('/code/output/output2.csv',index = False, header =False)

#Question3
for  i in range(0,3):
    model.add_cpds(cpds[i])
#create a Bayesian model and run variable elimination algorithm on it
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination
model_inference = VariableElimination(model)
query = model_inference.map_query(variables = ['tasty'])
#Expected Output
print (query)
result = pd.DataFrame(query,index=[0])
#write you output to csv
result.to_csv('/code/output/output3.csv',index = False)
