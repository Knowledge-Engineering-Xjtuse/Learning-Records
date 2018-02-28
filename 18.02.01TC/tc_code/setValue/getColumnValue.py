#-*- coding: UTF-8 -*-
from dataToMysql import *
fw = open('result.txt', 'w')
sql = "select * from newinfo"
data, result = getData(sql)
for i in xrange(32):
    s = []
    for index in range(data):
        if result[index][i] not in s:
            s.append(result[index][i])
    fw.write("列号:"+ str(i+1) + "\n总量为:" + str(len(s))+ "\n集合为:")
    for index in range(len(s)):
        fw.write(s[index] + "  ")
    fw.write("\n")
fw.close()
print "写入完毕"