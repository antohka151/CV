import cv2 as cv
import numpy as np

img = cv.imread(r"Example of work\1.jpg", cv.IMREAD_GRAYSCALE)
img_new = img.copy()
pattern = np.array([[-1, 0, 1],
                    [-1, 0, 1],
                    [-1, 0, 1]])
rad = int(len(pattern) / 2)

for i in range(rad, img.shape[1] - rad):
    for j in range(rad, img.shape[0] - rad):
        img_new[j][i] = 0 if 256 / 10 > (np.array([[a[i + c] for c in range(-rad, rad + 1)]
                                                   for a in img[j - rad:j + rad + 1]]) * pattern).sum() else 255

cv.imwrite("1_lzr.jpg", img_new)
