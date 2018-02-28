#-*- coding: UTF-8 -*-
from dataToMysql import *
s = []
# id = '=' + row['front_track'] + "+" + row['rated_passenger'] + "+" + row['equipment_quality'] + "+" + row[
#                 'total_quality'] + "+" + row['car_height'] + "+" + row['car_length'] + "+" + row[
#                      'engine_torque'] + "+" + row['power'] + "+" + row['emission_standards_id'] + "+" + row[
#                      'gearbox_type'] + "+" + row['TR']
sql = "select class_id,front_track,rated_passenger,equipment_quality,total_quality,car_height,car_length,engine_torque,power,emission_standards_id,gearbox_type,TR,sale_date from newinfo ORDER by sale_date asc"
data, result = getData(sql)
n = 0
for index in range(data):
    # if result[index][0] not in s:
    #     s.append(result[index][0])
    a = result[index][0] + "+" + result[index][1] + "+" + result[index][2] + "+" + result[index][3] + "+" + result[index][4] + "+" + result[index][5] + "+" + result[index][6] + "+" + result[index][7] + "+" + result[index][8] + "+" + result[index][9] + "+" + result[index][10] + "+" + result[index][11]
    if a in s:
        n = n + 1
    s.append(a)
print n
fw = open('id.txt', 'w')
for index in range(len(s)):
    fw.write(s[index] + "\n")
fw.close()
print "写入完毕"