import pickle
import numpy as np


class PredictDisease:
    def __init__(self):
        self.data_model = pickle.load(open('MainML\\final_pharma_3.sav', 'rb'))
        self.disease = pickle.load(open('MainML\\r_disease_3.sav', 'rb'))
        self.symptoms = pickle.load(open('MainML\\r_symptoms_3.sav', 'rb'))

        self.symptoms_list = list(self.symptoms.keys())

    def get_symptoms_list(self):
        return self.symptoms_list

    def predict_disease(self, s_list):
        user = np.zeros((1, 404), dtype=int)
        for ds in s_list:
            user[0, self.symptoms[ds]] = 1
        y_pred = self.data_model.predict(user)
        if self.disease[y_pred[0]] == 'none':
            return 'disease not detectable'
        else:
            return self.disease[y_pred[0]]
