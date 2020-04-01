import numpy as np
import pandas as pd

dataset=pd.read_csv('/content/drive/My Drive/TECHNOUTSAV/OHAS Dataset.csv')
#print(dataset)
#a=dataset['Symptoms']
#print(list(dataset.columns))
#print( pd.isnull(dataset).sum()  )
dataset=dataset.dropna(axis=0,how='any',subset=['Symptoms'])
#print( pd.isnull(dataset).sum()  )
X=dataset.iloc[:, 0:1].values#disease
# l = sorted(np.unique(X))
# print(np.unique(X))
# a = dict()
# for i in range(0,len(l)):
#     a[i]=l[i]
# print(a)
Y=dataset.iloc[:, 8:9].values#age
Z=dataset.iloc[:, 9:10].values#gender
S=dataset.iloc[:, 12:13].values#season
m=dataset.iloc[:, 2:3].values#Symptoms
# print(sorted(np.unique(m)))
# m=sorted(np.unique(m))
# m=pd.unique(m)
# print(sorted(m))
# print(len(m))
# for i in range(0,len(m)):
#     a[i]=m[i]
# print(a)
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder()
m=labelencoder.fit_transform(m)
print(m)
Z=(labelencoder.fit_transform(Z)).reshape(-1, 1)
S=(labelencoder.fit_transform(S)).reshape(-1, 1)
X=(labelencoder.fit_transform(X)).reshape(-1, 1)
#print(S)
#print(sorted(m))
m=m.reshape(-1, 1)
en = OneHotEncoder(drop='first')
m = en.fit_transform(m)
m=m.toarray()
#print(m.shape)
Y=np.append(m,Y,axis=1)
Y=np.append(Y,Z,axis=1)
Y=np.append(Y,S,axis=1)
# #from sklearn.model_selection import train_test_split
# #X_train,X_test,Y_train,Y_test=train_test_split(Y,X,test_size=0.25,random_state=0);
# #----------------Model Prepration-----------------------------
from sklearn.utils import shuffle
X1, Y1 = shuffle(Y, X)
#
# # Fitting Kernel SVM to the Training set
# # from sklearn.svm import SVC
# # classifier = SVC(kernel = 'rbf', random_state = 0)
# # classifier.fit(Y, X)
# # Y_pred = classifier.predict(X1[0:5,:])
#
# # from sklearn.naive_bayes import GaussianNB
# #
# # gaussian = GaussianNB()
# # gaussian.fit(Y, X)
# # Y_pred = gaussian.predict(X1[0:5, :])
# # # Predicting the Test set results
from sklearn.metrics import accuracy_score
# # acc_randomforest = round(accuracy_score(Y_pred, Y1[0:5,:]) * 100, 2)
# # print( "MODEL-7: Accuracy of RandomForestClassifier : ",acc_randomforest)
#
from sklearn.ensemble import GradientBoostingClassifier

gbk = GradientBoostingClassifier()
gbk.fit(Y, X)
Y_pred = gbk.predict(X1[0:5, :])
acc_gbk = round(accuracy_score(Y_pred, Y1[0:5, :]) * 100, 2)
print( "MODEL-10: Accuracy of GradientBoostingClassifier : ",acc_gbk )
#print(Y_test.shape)
Y_pred = gbk.predict(Y[0:1, :])
print(Y_pred,' Which id actually ',X[0,:])
# #Making the Confusion Matrix
# # from sklearn.metrics import confusion_matrix
# # cm = confusion_matrix(Y_test, Y_pred)
# # print(cm)
#