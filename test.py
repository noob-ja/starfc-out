from scipy.io import loadmat
import numpy as np
import cv2
import os

point_path = './cat2k/'
image_path = './Stimuli/'

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)

for cat in os.listdir(point_path):
    cat = 'Action'
    mat_path = os.path.join(point_path, cat)
    im_path  = os.path.join(image_path, cat)
    for i in range(1,200,2):
        if i<10:
            i = '00'+str(i)
        elif i<100:
            i = '0'+str(i)
        else:
            i = str(i)
        mat = loadmat(os.path.join(mat_path,i)+'.mat')
        points = np.array(mat['img'].T, dtype=np.uint16)

        img = cv2.imread(os.path.join(im_path, i)+'.jpg')
        print('image: ', img.shape, 'pts: ', len(points))

        img[points[0][1]-5:points[0][1]+5, points[0][0]-5:points[0][0]+5] = [0, 0, 255]
        for j in range(1, len(points)):
            p1 = points[j-1]
            p2 = points[j]
            print(p1, p2)
            img[p2[1]-5:p2[1]+5, p2[0]-5:p2[0]+5] = [0, 0, 255]
            cv2.line(img, tuple(p1), tuple(p2), (0,0,255), 2)

        cv2.imshow('image', img)
        cv2.waitKey(0)
