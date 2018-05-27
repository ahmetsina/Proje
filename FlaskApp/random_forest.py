from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

import csv
import numpy as np
with open("FeatureExtraction/gender_labels.csv") as f:
    gender_labels = []
    reader = csv.reader(f)
    for i in reader:
        gender_labels.append(i)
        print(i)


with open("FeatureExtraction/hog.csv") as f:
    hog_results = []
    reader = csv.reader(f)
    for i in reader:
        hog_results.append(i)
        print(i)

with open("FeatureExtraction/gender_labels_test.csv") as f:
    gender_labels_test = []
    reader = csv.reader(f)
    for i in reader:
        gender_labels_test.append(i)
        print(i)


with open("FeatureExtraction/hog_test.csv") as f:
    hog_results_test = []
    reader = csv.reader(f)
    for i in reader:
        hog_results_test.append(i)
        print(i)



X = hog_results
Y = gender_labels

# Random Forest

rf = RandomForestClassifier(max_depth=17, random_state=1, n_estimators=18,min_samples_leaf=1)
rf.fit(X, np.array(Y).ravel())
joblib.dump(rf,"hog_rf.pkl")
sc = rf.score(hog_results_test, gender_labels_test)
print(sc)
