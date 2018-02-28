#-*- coding: UTF-8 -*-
import time
from skimage import io
from matplotlib.font_manager import FontProperties
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import csv

#将原始数据得到的字典转化为图表(X=sale_date,Y=sale_quantity,title=class_id)
def zidian(path="../data/test.csv"):
    new_dict = {}
    with open(path, 'r')as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
        for row in data:
            id = '=' + row['id'] + "=" + row['front_track'] + "+" + row['rated_passenger'] + "+" + row['equipment_quality'] + "+" + row[
                'total_quality'] + "+" + row['car_height'] + "+" + row['car_length'] + "+" + row[
                     'engine_torque'] + "+" + row['power'] + "+" + row['emission_standards_id'] + "+" + row[
                     'gearbox_type'] + "+" + row['TR']
            item = new_dict.get(row['class_id'], dict())
            item[row['sale_date']+id] = {k: row[k] for k in ('sale_quantity', 'price')}
            new_dict[row['class_id']] = item
    return new_dict

def sortYearList(data):
    # {
    #   '789290': ['201703', '201704', '201705', '201706', '201707', '201708', '201709', '201710'],
    #   '569154': ['201611', '201612', '201701', '201702', '201703', '201704']
    # }
    result = {}
    for class_id, values in data.items():
        yearList = []
        for sale_date_id, orders in values.items():
            year = sale_date_id.split('=')
            if year[0] not in yearList:
                yearList.append(year[0])
        result[class_id] = sorted(yearList)
    return result

data = zidian()
yearList = sortYearList(data)
for class_id_yearList, values_yearList in yearList.items():
    for class_id_data, values_data in data.items():
        if class_id_data == class_id_yearList:
            sum = 0
            for index in range(len(values_yearList)):
                number = 0
                for sale_date_id, orders in values_data.items():
                    year = sale_date_id.split('=')
                    if year[0] == values_yearList[index]:
                        number = number + 1
                sum = sum + number
            print class_id_data,sum
print 'finish'
# name_list = ['Monday', 'Tuesday', 'Friday', 'Sunday']
# num_list = [1.5, 0.6, 7.8, 6]
# num_list1 = [1, 2, 3, 1]
# x = list(range(len(num_list)))
# total_width, n = 0.2, 2
# width = total_width / n
#
# plt.bar(x, num_list, width=width, label='boy', fc='y')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list1, width=width, label='girl', tick_label=name_list, fc='r')
# plt.legend()
# plt.show()