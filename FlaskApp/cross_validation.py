from sklearn import svm
from detect_faces import facecrop
from hog import hog
import cv2
import numpy as np
from numpy.linalg import norm
import csv
import os
import pandas as pd
import re
arr = os.listdir("FeatureExtraction/images/test_images")

# Uncomment if did not cropped images
#for i in arr:
#    print(i #    facecrop("FeatureExtraction/images/test_images/" + i)


# Move cropped images to cropped directory
files = os.listdir("FeatureExtraction/images/cropped_test_images")
for file in files :
    fname, ext = os.path.splitext(file)
    if re.search("_cropped",str(file)):
        old_file = os.path.join("FeatureExtraction/images/cropped_test_images", fname + ext)
        new_file = os.path.join("FeatureExtraction/images/cropped_test_images", fname.replace("_cropped","") + ext)
        os.rename(old_file, new_file)

## Gerçek Cinsiyet degerlerini CSV olarak dondurme
image_file_names = os.listdir("FeatureExtraction/images/cropped_test_images")

dataFrame = pd.read_excel("FeatureExtraction/eth_gender_anno_all.xlsx", index_col=None)
df = pd.DataFrame.as_matrix(dataFrame)

labels = np.ones(len(image_file_names))
image_names = []
for i in df:
    image_names.append(i[0] + ".JPG")

for i in range(1, len(image_file_names)):
    index = image_names.index(image_file_names[i])
    labels[i] = df[index][3]

with open("FeatureExtraction/gender_labels_test.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    for i in labels:
        writer.writerow([i])


images_path = os.listdir("FeatureExtraction/images/cropped_test_images")
images_hog = []
for i in images_path:
    image_path = "FeatureExtraction/images/cropped_test_images/"+i
    print(image_path)
    image = cv2.imread(image_path, 0)
    images_hog.append(hog(image))

with open("FeatureExtraction/hog_test.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(images_hog)


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


