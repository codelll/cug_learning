import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2 as cv
import os

root = '..\\data\\potsdam\\labels'

# labels = list(sorted(os.listdir(os.path.join(root, "0.png"))))
def compire(list1,list2):
    if(list1[0] == list2[0]):
        if(list1[1] == list2[1]):
            if(list1[2] == list2[2]):
                return True
            else:return False
        else:return False
    else: return False

def convert_to_8bit(dir):
    label = cv.imread(dir)
    for i in range(len(label)):
        for j in range(len(label[i])):
            if compire(label[i][j],np.array([255,0,0])):
                label[i][j] = np.array([0])
            elif compire(label[i][j],np.array([255,255,0])):
                label[i][j] = np.array([1])
            elif compire(label[i][j],np.array([0,255,0])):
                label[i][j] = np.array([2])
            elif compire(label[i][j],np.array([0,255,255])):
                label[i][j] = np.array([3])
            elif compire(label[i][j],np.array([0,0,255])):
                label[i][j] = np.array([4])
            elif compire(label[i][j],np.array([255,255,255])):
                label[i][j] = np.array([5])
    B,G,R = cv.split(label)
    return R.astype(np.uint8)


labels = list(sorted(os.listdir(root)))
for i in range(len(labels)):
    label_path = os.path.join(root, labels[i])
    Image.fromarray(convert_to_8bit(label_path)).save("..//data//8bit//" + labels[i])
    print(i)

# cv.imwrite("..//data//8bit//"+"0.png",convert_to_8bit("../data//potsdam//labels//0.png"))
# for i in range(len(labels)):
#     label_path = os.path.join(root, "Masks", labels[i])
#     label = cv.imread(label_path)
#     B, G, R = cv.split(label)
#     # R = np.array(R)/255.0
#     R = R.astype(np.uint8)
#     Image.fromarray(R).save('./8bit/' + labels[i])
#     # cv.imwrite('./8bit/'+labels[i],R)