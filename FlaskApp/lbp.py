# import the necessary packages
from skimage import feature
import numpy as np
from sklearn.svm import LinearSVC
from imutils import paths
import os
import cv2
import csv

class LocalBinaryPatterns:
	def __init__(self, numPoints, radius):
		# store the number of points and radius
		self.numPoints = numPoints
		self.radius = radius

	def describe(self, image, eps=1e-7):
		# compute the Local Binary Pattern representation
		# of the image, and then use the LBP representation
		# to build the histogram of patterns
		lbp = feature.local_binary_pattern(image, self.numPoints,
			self.radius, method="uniform")
		(hist, _) = np.histogram(lbp.ravel(),
			bins=np.arange(0, self.numPoints + 3),
			range=(0, self.numPoints + 2))

		# normalize the histogram
		hist = hist.astype("float")
		hist /= (hist.sum() + eps)

		# return the histogram of Local Binary Patterns
		return hist



# initialize the local binary patterns descriptor along with
# the data and label lists
desc = LocalBinaryPatterns(48,16)
data = []
labels = []



path = "/Users/ahmetsina/PycharmProjects/GenderAnalyzer/FeatureExtraction/images/aligned_cropped_test_images"
images_path = os.listdir(path)
images_lbp = []
for i in images_path:
    imagePath = path + "/" + i
    print(imagePath)
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    images_lbp.append(hist)

with open("FeatureExtraction/lbp_aligned_test.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(images_lbp)
# train a Linear SVM on the data





model = LinearSVC(C=100.0, random_state=42)
model.fit(data, labels)
