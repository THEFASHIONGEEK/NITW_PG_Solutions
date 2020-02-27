import re
import warnings
from string import punctuation

import mglearn as mg
import nltk
import numpy as np
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

warnings.filterwarnings("ignore")

# Loading the dataset
data = pd.read_csv("abcnews-date-text.csv", error_bad_lines=False)
data_text = data[["headline_text"]]
data_text["index"] = data_text.index
documents = data_text

cnt_data = list(data.headline_text.values)
count_vectorizer = CountVectorizer(
    max_df=0.95, min_df=2, max_features=1000, ngram_range=(1, 2), stop_words="english"
)
cv_data = count_vectorizer.fit_transform(cnt_data)
lda_model = LatentDirichletAllocation(n_components=5)
lda = lda_model.fit_transform(cv_data)


sorting = np.argsort(lda_model.components_)[:, ::-1]
features = np.array(count_vectorizer.get_feature_names())
mg.tools.print_topics(
    topics=range(5),
    feature_names=features,
    sorting=sorting,
    topics_per_chunk=5,
    n_words=25,
)
