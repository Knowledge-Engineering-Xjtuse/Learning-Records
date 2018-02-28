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

fw = open('class_id.txt', 'r')
# 103507=201503=17=1557+5+1510+1930+1630+4270+192+118+3+AT+6
class_id = []
for line in fw.readlines():
    class_id.append(line.strip())
print 'class_id:', len(class_id)
fw.close()

date = []

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_dict = {}
fw = open('all_sum.txt', 'w')
for k in class_id:
    res = ''
    Y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    G = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    K = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in data:
        result = j.split('=')
        if result[0] == k:
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
    for index in range(12):
        res = res + str(Y[index]) + '-'
    for index in range(12):
        res = res + str(R[index]) + '-'
    for index in range(12):
        res = res + str(G[index]) + '-'
    for index in range(12):
        res = res + str(K[index]) + '-'
    for index in range(12):
        res = res + str(B[index]) + '-'
    for index in range(12):
        res = res + str(C[index]) + '-'
    fw.write(k + ':' + res + "\n")
fw.close()
print "写入完毕"
    # plt.figure(figsize=(19.20, 9.44))
    # width = 0.1
    # if title == 1320:
    # for i in range(len(X)):
    #     X[i] = X[i] + width
    # plt.bar(X, Y, width=width, label='boy', fc='y')
    # for i in range(len(X)):
    #     X[i] = X[i] + width
    # plt.bar(X, R, width=width, label='boy', fc='r')
    # for i in range(len(X)):
    #     X[i] = X[i] + width
    # plt.bar(X, G, width=width, label='boy', fc='g')
    # for i in range(len(X)):
    #     X[i] = X[i] + width
    # plt.bar(X, K, width=width, label='boy', fc='k')
    # for i in range(len(X)):
    #     X[i] = X[i] + width
    # plt.bar(X, B, width=width, label='boy', fc='b')
    # for i in range(len(X)):
    #     X[i] = X[i] + width
    # plt.bar(X, C, width=width, label='boy', fc='c')
    # for i in range(len(X)):
    #     X[i] = X[i] + width
    # plt.xticks(X, L, rotation=0)
    # plt.title(k)
    # plt.xlabel('date')
    # plt.ylabel('sale_date')
    # plt.grid(True)
    # p1 = r'C:\Users\lzp\Desktop\a\\' + str(k) + '.png'
    # plt.savefig(p1)