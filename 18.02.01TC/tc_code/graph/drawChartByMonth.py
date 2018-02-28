#-*- coding: UTF-8 -*-
import time
from skimage import io
from matplotlib.font_manager import FontProperties
from common_list import *
import matplotlib.pyplot as plt
import pandas as pd
from dataToMysql import *

class_id = []
fr = open('../entity/class_id.txt', 'r')
for line in fr.readlines():
    tmp = line.strip('\n')
    class_id.append(tmp)
fr.close()
x = [1,2,3,4,5,6,7,8,9,10,11,12]
# sale_date = []
# sale_quantity = []
for index in range(len(class_id)):
    year = []
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    sql = "select * from newInfo where class_id = '%s' order by  sale_date asc" % class_id[index]
    data, result = getData(sql)
    for i in range(data):
        # sale_date.append(float(result[i][0]))
        # sale_quantity.append(float(result[i][2]))
        years = (result[i][0])[0:4]
        month = int((result[i][0])[4:6])
        if years not in year:
            print "正在运行"
            if sum(y) != 0:
                plt.figure(figsize=(19.20, 9.44))
                # plt.plot(x, y, '.r')
                plt.plot(x, y)
                # 图片保存路径
                p1 = r'C:\Users\lzp\Desktop\a\\' + class_id[index] + "--" + str(year[-1:]) + '.png'
                img = io.imread('C:\Users\lzp\Desktop\\a\index.png')
                font = FontProperties(fname=r"D:\PythonProgram\scada\font\vista.ttf", size=14)
                plt.xlabel(u"车型ID:" + class_id[index] + u"--年份:" + str(year[-1:]), fontproperties=font)
                plt.ylabel(u"销量:", fontproperties=font)
                plt.savefig(p1)
            y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            year.append(years)
            y[month - 1] = float(result[i][2])
        else:
            y[month - 1] = y[month - 1] + float(result[i][2])
        if i == data-1:
            if sum(y) != 0:
                plt.figure(figsize=(19.20, 9.44))
                # plt.plot(x, y, '.r')
                plt.plot(x, y)
                # 图片保存路径
                p1 = r'C:\Users\lzp\Desktop\a\\' + class_id[index] + "--" + str(year[-1:]) + '.png'
                img = io.imread('C:\Users\lzp\Desktop\\a\index.png')
                font = FontProperties(fname=r"D:\PythonProgram\scada\font\vista.ttf", size=14)
                plt.xlabel(u"车型ID:" + class_id[index] + u"--年份:" + str(year[-1:]), fontproperties=font)
                plt.ylabel(u"销量:", fontproperties=font)
                plt.savefig(p1)
print "完成"

