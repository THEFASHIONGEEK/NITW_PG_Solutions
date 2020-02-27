import pandas as pd
df  = pd.read_excel("ReviewsFileName.xlsx")
from nltk.stem import PorterStemmer
import re
from nltk.corpus import stopwords
import numpy as np
cachedStopWords = stopwords.words("english")
stemmer = PorterStemmer()
def pre_process_data(data, remove_stop_words=True):

    list_Sentiment = []
    list_Review = []
    len_data = len(df)
    i=0
    
    for row in df.iterrows():
        i+=1
        if i % 500 == 0:
            print("%s | %s rows" % (i, len_data))

        ##### Remove and clean comments
        posts = row[1].Review
        temp = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', posts)
        temp = re.sub("[^a-zA-Z]", " ", temp)
        temp = re.sub(' +', ' ', temp).lower()
        if remove_stop_words:
            temp = " ".join([stemmer.stem(w) for w in temp.split(' ') if w not in cachedStopWords])
        else:
            temp = " ".join([stemmer.stem(w) for w in temp.split(' ')])
        list_Sentiment.append(row[1].Sentiment)
        list_Review.append(temp)

    #del data
    list_Review = np.array(list_Review)
    list_Sentiment = np.array(list_Sentiment)
    return list_Review, list_Sentiment
list_Review, list_Sentiment = pre_process_data(df, remove_stop_words=True)
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
cntizer = CountVectorizer()
X_cnt = cntizer.fit_transform(list_Review)
reverse_dic = {}
for key in cntizer.vocabulary_:
    reverse_dic[cntizer.vocabulary_[key]] = key
top_30 = np.asarray(np.argsort(np.sum(X_cnt, axis=0))[0,-30:][0, ::-1]).flatten()
top_30words = [reverse_dic[v] for v in top_30]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(list_Review, list_Sentiment, test_size=0.33, random_state=42)
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
clf=Pipeline([
        ('tfidf_vectorizer', TfidfVectorizer(ngram_range= (1,2),max_df=0.3,min_df=7)),
        ('rf_classifier', RandomForestClassifier(n_estimators=500,verbose=1,n_jobs=-1))
    ])
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred).tofile('cfmatrix.txt',sep=',')


