#-*- coding: UTF-8 -*-

import numpy as np
from pandas import Series
import statsmodels.api as sm
import csv

dataFile = open("all_sum.txt", "r")
reader = csv.reader(dataFile)  # 返回的是迭代类型
data = []
for item in reader:
    data.append(item[0][0:-1])
dataFile.close()
for i in range(len(data)):
    result = data[i].split(':')
    class_id = result[0]
    value = result[1].split('-')
    if int(value[68]) >= int(value[69]):
        a = (int(value[68]) + int(value[69]))/2
    else:
        a = (2 * int(value[69]) - int(value[68]))

    print class_id, a

# csvFile = open('test.csv', 'w', newline='')
# writer = csv.writer(csvFile)
# writer.writerow(['date','sale'])
# # for i in range(len(data)):
# #     result = data[i].split('-')
# #     for j in range(len(result)):
# csvFile.close()

# with open('test.csv', 'wb') as csv_file:
#     writer = csv.DictWriter(csv_file, ['header1', 'header2'])
#     writer.writeheader()
#     writer.writerow([1,2])