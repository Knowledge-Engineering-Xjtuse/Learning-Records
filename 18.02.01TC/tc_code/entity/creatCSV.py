#-*- coding: UTF-8 -*-

import pandas as pd
from pandas import DataFrame

data = '281301:965-650-745-759-863-679-891-606-767-841-1044-679-1555-825-686-826-1169-701-927-775-891-906-905-738-1073-759-759-702-723-671-722-687-927-737-871-664-1204-745-723-649-657-547-613-555-796-694-643-694-948-474-562-496-373-511-505-605-687-708-606-1102-795-410-715-548-569-554-621-584-584-329-0-0'
date = []
for i in range(6):
    year = 2012 + i
    for j in range(12):
        if j < 9:
            value = str(year) + '-0' + str(j+1)
        else:
            value = str(year) + '-' + str(j + 1)
        date.append(value)

sale = data.split(':')[1].split('-')

dataframe = DataFrame()
dataframe['date'] = date
dataframe['sale'] = sale
dataframe.to_csv('dataFinala.csv')