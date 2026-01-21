import os
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_path_1 = os.path.join(BASE_DIR, 'data', 'lm', 'test', '000001', 'rgb', '000000.png')
img_path_2 = os.path.join(BASE_DIR, 'data', 'lm', 'test', '000001', 'rgb', '000001.png')

img1 = cv.imread(img_path_1, cv.IMREAD_GRAYSCALE) # queryImage
img2 = cv.imread(img_path_2, cv.IMREAD_GRAYSCALE) # trainImage

if img1 is None or img2 is None:
    print('Could not open or find the image:')
    exit(0)

# Initialize ORB detector 
orb = cv.ORB_create()

# Find the keypoints and compute the descriptorswith ORB 
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=False)

# Match descriptors with KnnMatch = 2
raw_matches = bf.knnMatch(des1, des2, k=2)

# Apply ratio test
good_matches = []

# Filter matches using the Lowe's ratio test
for m, n in raw_matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)
matches = good_matches

print("Raw matches:", len(raw_matches))
print("Good matches:", len(good_matches))

# Draw first 10 matches
img3 = cv.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.imshow(img3), plt.axis('off')
plt.show()

