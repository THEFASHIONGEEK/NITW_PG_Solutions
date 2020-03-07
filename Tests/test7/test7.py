import pandas as pd
df = pd.read_csv("training-Eopinions/Eopinions.csv")
print(df['class'].value_counts())
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(40,20))
plt.xticks(fontsize=24, rotation=0)
plt.yticks(fontsize=24, rotation=0)
sns.countplot(data=df, x='class')
from sklearn.preprocessing import LabelEncoder

unique_type_list = ['Camera', 'Auto']
lab_encoder = LabelEncoder().fit(unique_type_list)

from nltk.stem import PorterStemmer
import re
from nltk.corpus import stopwords
import numpy as np
cachedStopWords = stopwords.words("english")
stemmer = PorterStemmer()
def pre_process_data(data, remove_stop_words=True):

    list_class = []
    list_text = []
    len_data = len(df)
    i=0
    
    for row in df.iterrows():
        i+=1
        if i % 100 == 0:
            print("%s | %s rows" % (i, len_data))

        ##### Remove and clean comments
        posts = row[1].text
        temp = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', posts)
        temp = re.sub("[^a-zA-Z]", " ", temp)
        temp = re.sub(' +', ' ', temp).lower()
        if remove_stop_words:
            temp = " ".join([stemmer.stem(w) for w in temp.split(' ') if w not in cachedStopWords])
        else:
            temp = " ".join([stemmer.stem(w) for w in temp.split(' ')])
        type_labelized = lab_encoder.transform([row[1]['class']])[0]
        list_class.append(type_labelized)
        list_text.append(temp)

    #del data
    list_text = np.array(list_text)
    list_class = np.array(list_class)
    return list_text, list_class
list_text, list_class = pre_process_data(df, remove_stop_words=True)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(list_text, list_class, test_size=0.2, random_state=42)
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
clf=Pipeline([
        ('cntizer_vectorizer', CountVectorizer()),
        ('rf_classifier', RandomForestClassifier(n_estimators=500,verbose=1,n_jobs=-1))
    ])
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred).tofile('cfmatrix.txt',sep=',')

import sklearn.metrics as metrics
# calculate the fpr and tpr for all thresholds of the classification
probs = clf.predict_proba(X_test)
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)

# method I: plt
import matplotlib.pyplot as plt
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()