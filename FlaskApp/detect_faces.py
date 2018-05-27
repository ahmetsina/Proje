import cv2
import os
import pandas as pd

import numpy as np
import csv

def facecrop(image):
    facedata = "FeatureExtraction/cascades/haarcascade_frontalface_alt2.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)
    if img is not None:
        minisize = (img.shape[1],img.shape[0])
        miniframe = cv2.resize(img, minisize)

        faces = cascade.detectMultiScale(miniframe)

        for f in faces:
            x, y, w, h = [ v for v in f ]
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

            sub_face = img[y:y+h, x:x+w]
            sub_face = cv2.resize(sub_face, (64,64))
            fname, ext = os.path.splitext(image)

            cv2.imwrite(fname+"_cropped"+ext, sub_face)
    else:
        print("Resim yuklenemedi")



    return

def replace_images(org_img_path, cropped_img_path ):
    arr = os.listdir(org_img_path)

    for i in arr:
        if "_cropped" in i:
            new_file_name = i.replace("_cropped", "")
            if not os.path.isfile(cropped_img_path + new_file_name):
                os.rename(org_img_path + i,
                          cropped_img_path + new_file_name)
                os.remove(org_img_path + i)
            else:
                print("Dosya zaten var")




arr = os.listdir("FeatureExtraction/images/test_images")
for i in arr:
    print(i)
    facecrop("FeatureExtraction/images/test_images/" + i)

for i in arr:
    if "_cropped" in i:
        new_file_name = i.replace("_cropped","")
        if not os.path.isfile("FeatureExtraction/images/cropped_images/"+new_file_name):
            os.rename("FeatureExtraction/images/org_images/"+i,"FeatureExtraction/images/cropped_images/"+new_file_name)
        else:
            print("Dosya zaten var")


image_file_names = os.listdir("FeatureExtraction/images/cropped_test_images")

dataFrame = pd.read_excel("FeatureExtraction/eth_gender_anno_all.xlsx",index_col=None)
df = pd.DataFrame.as_matrix(dataFrame)

labels = np.ones(len(image_file_names))
image_names = []
for i in df:
    image_names.append(i[0] + ".JPG")

for i in range(1,len(image_file_names)):
    index = image_names.index(image_file_names[i])
    labels[i] = df[index][3]



with open("FeatureExtraction/gender_labels_test.csv","w") as f:
    writer = csv.writer(f, delimiter=",")
    for i in labels:
        writer.writerow([i])



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