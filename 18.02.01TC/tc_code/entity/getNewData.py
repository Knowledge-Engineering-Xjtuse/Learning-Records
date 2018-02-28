# -*- coding: UTF-8 -*-

fw = open('all.txt', 'r')
# 789290=201709=4039=1460+5+1090+1500+1490+4440+140+79+1+CVT+0=46
data = []
for line in fw.readlines():
    data.append(line.strip())
print 'data:', len(data)
fw.close()

fw = open('sum_id.txt', 'r')
# 2014-5025-362
sum_id = []
sumId = []
for line in fw.readlines():
    sum_id.append(line.strip())
    result = line.strip().split('-')
    if result[0] not in sumId:
        sumId.append(result[0])
        sumId.append(result[1])
print 'sum_id:', len(sumId)
fw.close()

# 789290=201709=4039=46
newData = []
for index in data:
    id = []
    result = index.split('=')
    if result[2] not in sumId:
        newData.append(result[0] + '=' + result[1] + '=' + result[2] + '=' + result[4] + '=' + result[3])
    else:
        for k in sum_id:
            value = k.split('-')
            if value[0] == result[2]:
                newData.append(result[0] + '=' + result[1] + '=' + result[2] + '=' + value[2] + '=' + result[3])
fw = open('getnewData.txt', 'w')
for index in range(len(newData)):
    fw.write(newData[index] + "\n")
fw.close()
print "写入完毕"


