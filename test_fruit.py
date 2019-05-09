from scipy.io import loadmat
import numpy as np
import cv2
import os

point_path = './fruit/'
image_path = './fruit_im/'

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)

for i in range(1,177):
    i = str(i)
    mat = loadmat(os.path.join(point_path,i)+'.mat')
    points = np.array(mat['img'].T, dtype=np.uint16)

    img = cv2.imread(os.path.join(image_path, i)+'.png')
    print('image: ', img.shape, 'pts: ', len(points))

    img[points[0][1]-1:points[0][1]+1, points[0][0]-1:points[0][0]+1] = [0, 0, 255]
    for j in range(1, len(points)):
        p1 = points[j-1]
        p2 = points[j]
        print(p1, p2)
        img[p2[1]-1:p2[1]+1, p2[0]-1:p2[0]+1] = [0, 0, 255]
        cv2.line(img, tuple(p1), tuple(p2), (0,0,255), 1)

    cv2.imshow('image', img)
    cv2.waitKey(0)
