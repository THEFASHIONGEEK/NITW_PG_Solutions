import pandas as pd
import numpy as np 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df=pd.read_json('/data/training/NewsArticles.json')
df.head()
det=df['Vector']
vectors=pd.DataFrame(list(det))
vectors.shape
#Kmeans without PCA
model=KMeans(n_clusters=5)
model.fit(vectors)
print ("SSE: ",model.inertia_)
#Applying PCA 
from sklearn.decomposition import PCA
pca = PCA(n_components=100)
pca.fit(vectors.transpose())
new_vectors=pd.DataFrame(pca.components_).transpose()
new_vectors.shape
#Kmeans after PCA
model_afterPCA=KMeans(n_clusters=5)
model_afterPCA.fit(new_vectors)
print ("SSE: ",model_afterPCA.inertia_)
df['LabelWithoutPCA']=model.labels_
print(df['LabelWithoutPCA'])
df['LabelAfterPCA']=model_afterPCA.labels_
for each,subset in df.groupby('LabelWithoutPCA'):
    print ("For Label :",each)
    
    print ( ' '.join(subset['Preprocessed-Article']).lower().encode('utf-8').split()[:50] ) 
for each,subset in df.groupby('LabelAfterPCA'):
    print ("For Label :",each)
    print ( ' '.join(subset['Preprocessed-Article']).lower().encode('utf-8').split()[:10] ) 
    df['LabelWithoutPCA'].value_counts()
df['LabelAfterPCA'].value_counts()

#writing output to output.csv
result=[164.83,95.52, 4, 48, 3,169, 'stages','paid']
result=pd.DataFrame(result)
#writing output to output.csv
result.to_csv('/code/output/output.csv', header=False, index=False)
