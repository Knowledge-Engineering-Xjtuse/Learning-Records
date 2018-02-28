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
# fw = open('train.txt', 'w')
# for i in data:
#     value = ''
#     result = i.split(':')
#     class_id = result[0]
#     sale_quantity = []
#     length = len(result[1]) - 1
#     res = result[1][0:length].split('-')
#     for k in range(len(res)):
#         if k < 68:
#             sale_quantity.append(int(res[k]))
#     for index in range(67):
#         if index == 66:
#             value = value + str(sale_quantity[index])
#         else:
#             value = value + str(sale_quantity[index]) + '-'
#     fw.write(class_id + ':' + value + "\n")
# fw.close()

# fw = open('test.txt', 'w')
# for i in data:
#     value = ''
#     result = i.split(':')
#     class_id = result[0]
#     sale_quantity = []
#     length = len(result[1]) - 1
#     res = result[1][0:length].split('-')
#     for k in range(len(res)):
#         if k >= 67 and k < 70:
#             sale_quantity.append(int(res[k]))
#     for index in range(3):
#         if index == 2:
#             value = value + str(sale_quantity[index])
#         else:
#             value = value + str(sale_quantity[index]) + '-'
#     fw.write(class_id + ':' + value + "\n")
# fw.close()