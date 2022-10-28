import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


class Classifier:
    """
    Class to classify data by ML algorithm
     :author: Kaulitz Guimaraes
    """
    classifierManager = None
    svm_bin = './Classifier2.bin'
    naive_bin = './Classifier.bin'

    def __init__(self, values, labels):
        """
        Class constructor
        """
        self.labels = labels
        self.classifier = None
        self.load_classifier(values)
        self.accuracy = None
        self.get_accuracy(values)
        self.save_classifier()

    def create_classifier(self):
        """
        This metho creates an instance of OneVsRestClassifier object
        :return:  OneVsRestClassifier
        """
        #         self.classifer =SVC(gamma='auto')
        self.classifier = LogisticRegression()

    def load_classifier(self, values):
        """
        This method loads a classifier by a serial if there is any, it trigger the classifier training
        :return: None
        """
        self.create_classifier()
        self.train_algorithm(values)

    def get_accuracy(self, values):
        y_pred = self.predict(values)
        self.accuracy = accuracy_score(self.labels, y_pred)

    @classmethod
    def open_classifier(cls):
        """
        This method  tries to open a serial classifier and loads it
        :return: None
        """
        try:
            with open(Classifier.naive_bin, 'rb') as f:
                Classifier.classifierManager = pickle.load(f)
            f.close()
        except Exception  as e:
            print(e)
            pass

    def train_algorithm(self, values):
        """
        This method trains the algorithm according with DATA API
        :return: void
        """
        self.classifier.fit(values, self.labels)

    def save_classifier(self):
        """
         This method save the classifier serialized
         :return: void
        """
        #        bin_file = open(Classifier.svm_bin, mode='wb')
        bin_file = open(Classifier.naive_bin, mode='wb')
        pickle.dump(self, bin_file)
        bin_file.close()

    def predict(self, bag_of_words):
        """
        This method predicts  the class of each dsta in the content list
        :param list_of_content: list
        :return: list
        """
        return self.classifier.predict(bag_of_words)