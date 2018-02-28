# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

fw = open('sum.txt', 'r')
# 103507=201503=17=1557+5+1510+1930+1630+4270+192+118+3+AT+6
data = []
for line in fw.readlines():
    data.append(line.strip())
print 'data:', len(data)
fw.close()

date = []
info = []
for index in data:
    result = index.split('=')
    if result[3] not in info:
        info.append(result[3])

title = 0
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for index in info:
    Y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    G = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    K = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label = ''
    c = ''
    title = title + 1
    year = []
    for j in data:
        result = j.split('=')
        if result[3] == index:
            label = str(result[0] + '-' + result[3])
            a = int(result[1][2:4]) - 12
            if a == 0:
                month = int(result[1][4:6]) - 1
                Y[month] = Y[month] + int(result[2])
            elif a == 1:
                month = int(result[1][4:6]) - 1
                R[month] = R[month] + int(result[2])
            elif a == 2:
                month = int(result[1][4:6]) - 1
                G[month] = G[month] + int(result[2])
            elif a == 3:
                month = int(result[1][4:6]) - 1
                K[month] = K[month] + int(result[2])
            elif a == 4:
                month = int(result[1][4:6]) - 1
                B[month] = B[month] + int(result[2])
            else:
                month = int(result[1][4:6]) - 1
                C[month] = C[month] + int(result[2])
    print label
    plt.figure(figsize=(19.20, 9.44))
    width = 0.1
    # x = list(range(len(X)))
    if title >= 1109 and title <= 1385:
        for i in range(len(X)):
            X[i] = X[i] + width
        plt.bar(X, Y, width=width, label='boy', fc='y')
        for i in range(len(X)):
            X[i] = X[i] + width
        plt.bar(X, R, width=width, label='boy', fc='r')
        for i in range(len(X)):
            X[i] = X[i] + width
        plt.bar(X, G, width=width, label='boy', fc='g')
        for i in range(len(X)):
            X[i] = X[i] + width
        plt.bar(X, K, width=width, label='boy', fc='k')
        for i in range(len(X)):
            X[i] = X[i] + width
        plt.bar(X, B, width=width, label='boy', fc='b')
        for i in range(len(X)):
            X[i] = X[i] + width
        plt.bar(X, C, width=width, label='boy', fc='c')
        for i in range(len(X)):
            X[i] = X[i] + width
        plt.xticks(X, L, rotation=0)
        plt.title(label)
        plt.xlabel('date')
        plt.ylabel('sale_date')
        plt.grid(True)
        p1 = r'C:\Users\lzp\Desktop\a\\' + str(title) + '.png'
        plt.savefig(p1)