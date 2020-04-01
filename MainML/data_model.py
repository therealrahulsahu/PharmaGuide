import pickle
import numpy as np


class PredictDisease:
    def __init__(self):
        self.data_model = pickle.load(open('MainML\\pharma_guide_finalized_model.sav', 'rb'))
        self.r_disease = pickle.load(open('MainML\\r_disease.sav', 'rb'))
        self.r_gender = pickle.load(open('MainML\\r_gender.sav', 'rb'))
        self.r_seasons = pickle.load(open('MainML\\r_seasons.sav', 'rb'))
        self.r_symptoms = pickle.load(open('MainML\\r_symptoms.sav', 'rb'))

        self.symptoms_list = list(self.r_symptoms.keys())

    def get_symptoms_list(self):
        return self.symptoms_list

    def predict_disease(self, disease_list, age, gender, season):
        user_input = [0 for _ in range(406)]
        for ds in disease_list:
            user_input[self.r_symptoms[ds] - 1] = 1
        user_input[403] = age
        user_input[404] = self.r_gender[gender]
        user_input[405] = self.r_seasons[season]
        test = np.array([user_input, ])

        y_pred = self.data_model.predict(test)
        return self.r_disease[y_pred[0]]
