#-*- coding: UTF-8 -*-
import csv

#将原始数据转化为字典（选取个别属性），形如：
# {'354068':
#     {'201611=1=2-MT-1-T-1-1308':
#         {
#             'price': '10.9',
#             'sale_quantity': '202'
#         }
#     },
#     {'201611=2=2-MT-1-T-1-1308':
#         {
#             'price': '10.9',
#             'sale_quantity': '202'
#         }
#     }
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

s = []
dictt = zidian()
for class_id, values in dictt.items():
    for sale_date_id, orders in values.items():
        for index, value in orders.items():
            if index == 'sale_quantity':
                s.append(class_id + '=' + sale_date_id + '=' + value)
fw = open('all.txt', 'w')
for index in range(len(s)):
    fw.write(s[index] + "\n")
fw.close()
sum = []
# s[0] : 789290=201709=4039=1460+5+1090+1500+1490+4440+140+79+1+CVT+0=46
for i in range(len(s)):
    a = s[i].split('=')
    for j in range(len(s)):
        b = s[j].split('=')
        if a[0]+a[1]+a[3] == b[0]+b[1]+b[3] and a[2] != b[2]:
            if b[2] + '-' + a[2] + '-' + str(int(b[4])+int(a[4])) not in sum:
                sum.append(a[2] + '-' + b[2] + '-' + str(int(b[4])+int(a[4])))
fw = open('sum_id.txt', 'w')
for index in range(len(sum)):
    fw.write(sum[index] + "\n")
fw.close()
print "写入完毕"