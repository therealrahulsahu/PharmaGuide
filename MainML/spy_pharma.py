import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('ohas.csv')
dataset = dataset.dropna(axis=0, how='any', subset=['Symptoms'])

disease = dataset.iloc[:, 0:1].values

age = dataset.iloc[:, 8:9].values
gender = dataset.iloc[:, 9:10].values
season = dataset.iloc[:, 12:13].values
symptoms = dataset.iloc[:, 2:3].values


labelencoder = LabelEncoder()
c_symptoms = labelencoder.fit_transform(symptoms).reshape(-1, 1)
c_gender = labelencoder.fit_transform(gender).reshape(-1, 1)
c_season = labelencoder.fit_transform(season).reshape(-1, 1)

Y = labelencoder.fit_transform(disease).reshape(-1, 1)

ohe = OneHotEncoder(drop='first')
dummy_sym = ohe.fit_transform(c_symptoms).toarray()

X = np.append(dummy_sym, age, axis=1)
X = np.append(X, c_gender, axis=1)
X = np.append(X, c_season, axis=1)

# print(symptoms[0][0])


def make_dict(in_data_1, in_data_2):
    out_data = {}
    try:
        i = 0
        while True:
            out_data[in_data_1[i][0]] = in_data_2[i][0]
            i += 1
    except IndexError:
        pass
    return out_data


r_symptoms = make_dict(symptoms, c_symptoms)
r_gender = make_dict(gender, c_gender)
r_seasons = make_dict(season, c_season)

r_disease = make_dict(Y, disease)

'''pickle.dump(r_symptoms, open('r_symptoms.sav', 'wb'))
pickle.dump(r_gender, open('r_gender.sav', 'wb'))
pickle.dump(r_seasons, open('r_seasons.sav', 'wb'))
pickle.dump(r_disease, open('r_disease.sav', 'wb'))'''
# from sklearn.utils import shuffle
# X1, Y1 = shuffle(Y, X)
# from sklearn.ensemble import GradientBoostingClassifier
# gbk = GradientBoostingClassifier()
# gbk.fit(Y, X)
# pickle.dump(gbk, open('re_'+filename, 'wb'))

loaded_model = pickle.load(open('pharma_guide_finalized_model.sav', 'rb'))

user_inp = [0 for _ in range(406)]
user_inp[r_symptoms['fever']-1] = 1
user_inp[r_symptoms['snuffle']-1] = 1
user_inp[403] = 24
user_inp[404] = 1
user_inp[405] = 0
test = np.array([user_inp, ])

Y_pred = loaded_model.predict(test)
print(r_disease[Y_pred[0]])
# Y_pred = gbk.predict(X1[0:5, :])
acc_gbk = round(accuracy_score(Y_pred, Y[0:100, :]) * 100, 2)
print("MODEL-10: Accuracy of GradientBoostingClassifier : ", acc_gbk)

# Y_pred = gbk.predict(Y[0:1, :])
# Y_pred = loaded_model.predict(Y[0:1, :])
# print(Y_pred,' Which id actually ',X[0,:])

master = min(age.reshape(1, -1)[0].tolist())
