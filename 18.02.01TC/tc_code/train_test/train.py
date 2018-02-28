# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

fr = open('train.txt', 'r')
# 425432:1994-1274-1283...
trainData = []
for line in fr.readlines():
    trainData.append(line.strip())
print 'trainData:', len(trainData)
fr.close()

fr = open('test.txt', 'r')
# 425432:1664-1539-1848
testData = []
for line in fr.readlines():
    testData.append(line.strip())
print 'testData:', len(testData)
fr.close()

temp = trainData[0].split(':')
X = np.linspace(1,67,67)
Y = []
for value in temp[1].split('-'):
    Y.append(int(value))

plt.figure(figsize=(19.20, 9.44))
plt.plot(X, Y)
plt.show()

