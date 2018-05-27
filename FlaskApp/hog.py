import os
import cv2
import numpy as np
from numpy.linalg import norm
import csv

def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)
    bin_n = 16 # Number of bins
    bin = np.int32(bin_n*ang/(2*np.pi))

    bin_cells = []
    mag_cells = []

    cellx = celly = 8

    for i in range(0,int(img.shape[0]/celly)):
        for j in range(0,int(img.shape[1]/cellx)):
            bin_cells.append(bin[i*celly : i*celly+celly, j*cellx : j*cellx+cellx])
            mag_cells.append(mag[i*celly : i*celly+celly, j*cellx : j*cellx+cellx])

    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)

    # transform to Hellinger kernel
    eps = 1e-7
    hist /= hist.sum() + eps
    hist = np.sqrt(hist)
    hist /= norm(hist) + eps

    return hist


path = "/Users/ahmetsina/PycharmProjects/GenderAnalyzer/FeatureExtraction/images/cropped_test_images"
images_path = os.listdir(path)
images_hog = []
for i in images_path:
    image_path = path+"/"+i
    print(image_path)
    image = cv2.imread(image_path, 0)
    images_hog.append(hog(image))

with open("FeatureExtraction/hog_test.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(images_hog)

