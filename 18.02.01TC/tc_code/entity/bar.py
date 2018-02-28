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
for index in info:
    X = []
    Y = []
    label = ''
    title = title + 1
    for j in data:
        result = j.split('=')
        if result[3] == index:
            label = str(result[0] + '-' + result[3])
            X.append(result[1][3:6])
            Y.append(int(result[2]))
    print label
    if title > 1376:
        plt.figure(figsize=(19.20, 9.44))
        width = 0.1
        x = list(range(len(X)))
        plt.bar(x, Y, width=width, label='boy', fc='y')
        plt.xticks(x, X, rotation=0)
        plt.title(label)
        plt.xlabel('date')
        plt.ylabel('sale_date')
        plt.grid(True)
        p1 = r'C:\Users\lzp\Desktop\a\\' + str(title) + '.png'
        plt.savefig(p1)
print title