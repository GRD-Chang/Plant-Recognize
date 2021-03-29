import os
import shutil

import scipy.io as scio
import numpy as np


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


for i in range(1, 103):
    path = "./102flowers/" + str(i)
    mkdir(path)

dataFile = 'D:/download/imagelabels.mat'
data = scio.loadmat(dataFile)
labels = np.array(data['labels'])

picPath = 'E:/大创/ResNet102/102flowers/jpg'
picNames = os.listdir(picPath)

for i in range(len(picNames)):
    oldPath = "E:/大创/ResNet102/102flowers/jpg/" + picNames[i]
    newPath = "E:/大创/ResNet102/102flowers/" + str(labels[0][i])
    shutil.move(oldPath, newPath)
