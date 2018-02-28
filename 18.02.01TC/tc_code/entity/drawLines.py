# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

fw = open('all_sum.txt', 'r')
# 425432:1994-1274-1283...
data = []
for line in fw.readlines():
    data.append(line.strip())
print 'data:', len(data)
fw.close()

# X = np.linspace(1,72,72)
X = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]
Y = []
a = 5
for i in data:
    result = i.split(':')
    class_id = result[0]
    sale_quantity = []
    length = len(result[1]) - a
    res = result[1][0:length].split('-')
    for k in range(len(res)):
        sale_quantity.append(int(res[k]))
    print class_id
    # plt.figure(figsize=(19.20, 9.44))
    # plt.plot(X, sale_quantity)
    # plt.xticks(X, X, rotation=0)
    # plt.xlabel('month')
    # plt.ylabel('sale_quantity')
    # plt.grid(True)
    # p1 = r'C:\Users\lzp\Desktop\a\\'+ class_id +'.png'
    # plt.savefig(p1)
    Y.append(sale_quantity)
plt.figure(figsize=(19.20, 9.44))
for values in Y:
    plt.plot(X,values)
plt.xticks(X, X, rotation=0)
plt.xlabel('month')
plt.ylabel('sale_quantity')
plt.grid(True)
p1 = r'C:\Users\lzp\Desktop\a\\sum.png'
plt.savefig(p1)