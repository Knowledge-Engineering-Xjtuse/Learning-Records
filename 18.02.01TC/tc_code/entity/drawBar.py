# -*- coding: UTF-8 -*-


fw = open('getnewData.txt', 'r')
# 789290=201709=4039=46=1460+5+1090+1500+1490+4440+140+79+1+CVT+0
data = []
for line in fw.readlines():
    data.append(line.strip())
print 'data:', len(data)
fw.close()

class_id = []
sale_date = []
for index in range(len(data)):
    result = data[index].split('=')
    if result[0] not in class_id:
        class_id.append(result[0])
    if result[1] not in sale_date:
        sale_date.append(result[1])

class_id = sorted(class_id)
sale_date = sorted(sale_date)

# 数据补全（缺省值）
allDate = []
for i in range(len(class_id)):
    for j in range(len(sale_date)):
        allDate.append(class_id[i] + '=' + sale_date[j])
sum = []
allNewDate = []
for i in range(len(allDate)):
    number = 0
    id = []
    for j in range(len(data)):
        result = data[j].split('=')
        if result[0] + '=' + result[1] == allDate[i]:
            if result[2] not in id:
                number = number + 1
                id.append(result[2])
                sum.append(result[0] + '=' + result[1] + '=' + result[3] + '=' + result[4])
                print result[0] + '=' + result[1] + '=' + result[3] + '=' + result[4]
    if number > 0:
        res = allDate[i].split('=')
        print res[0] + '-' + res[1] + '-' + str(number)
        allNewDate.append(res[0] + '=' + res[1] + '=' + str(number))
fw = open('allDataNum.txt', 'w')
for index in range(len(allNewDate)):
    fw.write(allNewDate[index] + "\n")
fw.close()
fw = open('sum.txt', 'w')
for index in range(len(sum)):
    fw.write(sum[index] + "\n")
fw.close()