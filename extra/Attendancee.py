import cv2
import numpy as np
import os


if __name__ == '__main__':
    name = input("enter image name")
    path = 'ImagesAttendance'
    # Read image
    im = cv2.imread(f'{path}/{name}')

    # Select ROI
    r = cv2.selectROI(im)

    # Crop image
    imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    # Display cropped image

    cv2.imshow("Image", imCrop)
    path = 'ImagesAttendance'
    cv2.imwrite(os.path.join(path, name), imCrop)
    #cv2.imwrite(name , imCrop)

    cv2.waitKey(0)