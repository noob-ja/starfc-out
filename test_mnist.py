from scipy.io import loadmat
import numpy as np
import cv2
import os

point_path = './mnist_test_output/'
image_path = './mnist_png/testing/'

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)

rad = 0

for cat in os.listdir(point_path):
    mat_path = os.path.join(point_path, cat)
    im_path  = os.path.join(image_path, cat)
    for f in os.listdir(mat_path):
        i = f.split('.')[0]
        mat = loadmat(os.path.join(mat_path,i)+'.mat')
        points = np.array(mat['img'].T, dtype=np.uint16)

        img = cv2.imread(os.path.join(im_path, i)+'.png')
        print('image: ', img.shape, 'pts: ', len(points))

        img[points[0][1]-rad:points[0][1]+rad, points[0][0]-rad:points[0][0]+rad] = [0, 0, 255]
        for j in range(1, len(points)):
            p1 = points[j-1]
            p2 = points[j]
            print(p1, p2)
            img[p2[1]-rad:p2[1]+rad, p2[0]-rad:p2[0]+rad] = [0, 0, 255]
            cv2.line(img, tuple(p1), tuple(p2), (0,0,255), 1)

        cv2.imshow('image', img)
        cv2.waitKey(0)
