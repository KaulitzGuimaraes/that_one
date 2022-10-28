import pickle

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
#TODO create a bow for all docments, clean trained data with it then train the model
from common.constants import BASE_DATA, TEXT_COL


class BOW:
    count_vect = CountVectorizer()
    tfidf_transformer = TfidfTransformer()
    cols = None
    bow = None

    def __init__(self, data=None):
        self.count_bag_train_t = self.create_bow(data, None)

    def save_bow(self):
        with(open('bow.bin', 'wb')) as b:
            pickle.dump(self, b)

    def create_bow(self, data=BASE_DATA, text_col=TEXT_COL):
        try:
            data = pickle.load(open(data, 'rb'))
            data = data[text_col]
        except:
            pass
        count_bag_train = self.count_vect.fit_transform(data)
        return self.tfidf_transformer.fit_transform(count_bag_train)

    def fit_to_bow(self, data, column=None):
        count_vector = CountVectorizer(vocabulary=self.count_vect.get_feature_names())
        count_bag_pred = count_vector.fit_transform(data[column] if column else data)
        return self.tfidf_transformer.fit_transform(count_bag_pred)

    @classmethod
    def get_bow(cls):
        cls.bow = pickle.load(open('bow.bin', 'rb'))
        return cls.bow

