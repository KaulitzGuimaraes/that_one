import pickle

import pandas as pd

from common.constants import TARGET_COL


class EmotionsIdentifier:
    emotions_map = None

    @classmethod
    def get_map(cls):
        print(type(cls.emotions_map))

        if isinstance(cls.emotions_map, type(None)):
            file = pickle.load(open('./merged_training.pkl', 'rb'))
            y, label = pd.factorize(file[TARGET_COL])
            cls.emotions_map = label
        return cls.emotions_map
