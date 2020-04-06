import numpy as np
import pandas as pd

dataset=pd.read_csv('ohas.csv')
dataset=dataset.dropna(axis=0,how='any',subset=['Symptoms'])

disease=dataset.iloc[:, 0:1].values #disease
l = sorted(np.unique(disease))
a = dict()
for i in range(0, len(l)):
    a[i] = l[i]
symptoms = dataset.iloc[:, 2:3].values #Symptoms
l = sorted(np.unique(symptoms))
b = dict()
for i in range(0, len(l)):
    b[i] = l[i]
#key = list(b.keys())
#values = list(b.values())
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_symptoms = LabelEncoder()
labelencoder_disease = LabelEncoder()
symptoms = labelencoder_symptoms.fit_transform(symptoms)
disease = (labelencoder_disease.fit_transform(disease)).reshape(-1, 1)

symptoms = symptoms.reshape(-1, 1)
en = OneHotEncoder()
symptoms = en.fit_transform(symptoms)
symptoms = symptoms.toarray()
de = np.zeros((1, (symptoms.shape[1]+1)), dtype=int)
k = np.array((1, (symptoms.shape[1])+1), dtype=int)
symptoms = symptoms.astype('int32')
x = disease[0]
flag = 0

print(symptoms.shape[1])
for i in range(0, len(disease)):
    if x == disease[i]:
        de_num = disease[i]
        for j in range(0, symptoms.shape[1]):
            de[0, j] = de[0, j] | symptoms[i, j]

        de[0, j+1] = de_num

    else:
        x = disease[i]
        if flag == 0:
            k = de.copy()
            de[:, :] = 0

        else:
            k = np.append(k, de, axis=0)
            de[:, :] = 0
        flag = 1

k = np.append(k, de, axis=0)

X_train = k[:, 0:404]
Y_train = k[:, 404:405]

x=np.random.randint(0,148)

from sklearn.utils import shuffle
X_test, Y_test = shuffle(X_train,Y_train)
X_test = X_test[0:5,:]
Y_test = Y_test[0:5,:]
x=np.random.randint(0,148)

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

randomforest = RandomForestClassifier()
randomforest.fit(X_train, Y_train)
Y_pred = randomforest.predict(X_test)
acc_randomforest = round(accuracy_score(Y_pred, Y_test) * 100, 2)
print( "MODEL-7: Accuracy of RandomForestClassifier : ",acc_randomforest  )
Y_pred = randomforest.predict(X_train[x:x+1, :])
print(Y_train.shape)
print(a[Y_pred[0]], ' Which is actually ',a[Y_train[x,0]])


# num = int(input('Number of symptoms'))

user = np.zeros((1, (symptoms.shape[1])), dtype=int)

# for i in range(0,num):
#     option = input('Enter symptoms')
#     user[0, key[values.index(option)]] = 1
#
# user[0,112]=1
# user[0,110]=1
# user[0,86]=1
# user[0,77]=1
# user[0,34]=1
# user[0,23]=1
# user[0,61]=1
# user[0,59]=1
# user[0,134]=1

user[0,142]=1
user[0,120]=1
user[0,136]=1
user[0,18]=1
user[0,79]=1
user[0,83]=1
user[0,67]=1
user[0,51]=1
user[0,43]=1

user[0, 67] = 1
user[0, 29] = 1
user[0, 36] = 1
user[0, 132] = 1
user[0, 147] = 1
user[0, 302] = 1
Y_pred = randomforest.predict(user)
print(a[Y_pred[0]])




rev_sym = {}
for idx in b:
    rev_sym[b[idx]] = idx


from pickle import dump
dump(randomforest, open('final_pharma_3.sav', 'wb'))
dump(a, open('r_disease_3.sav', 'wb'))
dump(rev_sym, open('r_symptoms_3.sav', 'wb'))
