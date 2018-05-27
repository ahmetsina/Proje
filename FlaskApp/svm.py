from sklearn import svm,linear_model
import os
import csv
import numpy as np
from sklearn.externals import joblib
from sklearn import metrics

with open("FeatureExtraction/gender_labels_aligned.csv") as f:
    gender_labels = []
    reader = csv.reader(f)
    for i in reader:
        gender_labels.append(i)
        print(i)


with open("FeatureExtraction/lbp_aligned.csv") as f:
    hog_results = []
    reader = csv.reader(f)
    for i in reader:
        hog_results.append(i)
        print(i)

X = hog_results
Y = gender_labels


with open("FeatureExtraction/gender_labels_aligned_test.csv") as f:
    gender_labels_test = []
    reader = csv.reader(f)
    for i in reader:
        gender_labels_test.append(i)
        print(i)


with open("FeatureExtraction/lbp_aligned_test.csv") as f:
    hog_results_test = []
    reader = csv.reader(f)
    for i in reader:
        hog_results_test.append(i)
        print(i)

# SVM

clf = svm.SVC(C=1000,probability=True)
clf.fit(X,np.array(Y).ravel())
joblib.dump(clf,'lbp_svm_aligned.pkl')
sc = clf.score(hog_results_test,gender_labels_test)
print(sc)








