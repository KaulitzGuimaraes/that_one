import  pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


count_vect = CountVectorizer()
tfidf_transformer = TfidfTransformer()

file : pd.DataFrame = pickle.load(open('merged_training.pkl', "rb"))
X_count= count_vect.fit_transform(file.text)
d = pd.DataFrame(X_count.A,columns=count_vect.get_feature_names_out())

file['categorical'] = pd.Categorical(file.emotions)
file['categorical'] = file.categorical.cat.codes

