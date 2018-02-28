#-*- coding: UTF-8 -*-

import numpy as np
import pandas as pd
from pandas import Series
from statsmodels.tsa.stattools import adfuller
from statsmodels.stats.diagnostic import acorr_ljungbox
from pandas import read_csv
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot
from pandas import DataFrame
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARMA
# 递归特征选择（Recursive Feature Selection，RFE）
# RFE 可以创建预测模型，对特征值赋予不同的权值，并删掉那些权重最小的特征，通过不断重复这一流程，最终就能得到预期数量的特征。
from sklearn.feature_selection import RFE

# 载入数据
# load dataset
series = Series.from_csv('dataFinal.csv', header=0)
# display first few rows
print(series.head(5))
# line plot of dataset
series.plot()
# pyplot.show()

# 平稳化-季节差分（周期为12）-差分运算成功消除了季节性变化和增长趋势信息
# seasonal difference
differenced = series.diff(12)
# trim off the first year of empty data
differenced = differenced[12:]
# save differenced dataset to file
differenced.to_csv('seasonally_adjusted.csv')
# plot differenced dataset
differenced.plot()
# pyplot.show()

# 自相关图-展示了每个滞后观察结果的相关性，以及这些相关性是否具有统计学的显着性
# plot_acf(series.dropna())
# plot_pacf(series.dropna())
# pyplot.show()
# ADF检验
# temp = np.array(series.dropna())
# t = adfuller(temp)
# output=pd.DataFrame(index=['Test Statistic Value', "p-value", "Lags Used", "Number of Observations Used","Critical Value(1%)","Critical Value(5%)","Critical Value(10%)"],columns=['value'])
# output['value']['Test Statistic Value'] = t[0]
# output['value']['p-value'] = t[1]
# output['value']['Lags Used'] = t[2]
# output['value']['Number of Observations Used'] = t[3]
# output['value']['Critical Value(1%)'] = t[4]['1%']
# output['value']['Critical Value(5%)'] = t[4]['5%']
# output['value']['Critical Value(10%)'] = t[4]['10%']
# print output
# Name: sale, dtype: int64
#                                  value
# Test Statistic Value          -3.10662
# p-value                      0.0260673
# Lags Used                           11
# Number of Observations Used         55
# Critical Value(1%)            -3.55527
# Critical Value(5%)            -2.91573
# Critical Value(10%)           -2.59567
# 单位根检验统计量对应的P值远小于0.05，故该序列可确认为平稳序列

# 序列的纯随机性检测
# print u'序列的纯随机性检测结果为：',acorr_ljungbox(series.dropna(),lags = 1)
# (array([ 4.21169782]), array([ 0.04014614]))

# # 时间序列到监督学习-这个过程可以在任意的时间步长下重复进行，例如6或24个月，感兴趣的朋友可以自行尝试。
# # load dataset
# series = Series.from_csv('seasonally_adjusted.csv', header=None)
# # reframe as supervised learning
# dataframe = DataFrame()
# for i in range(12,0,-1):
#     # i = 11, 10...
#     dataframe['t-'+str(i)] = series.shift(i)
# dataframe['t'] = series.values
# print(dataframe.head(13))
# dataframe = dataframe[13:]
# # save to new file
# dataframe.to_csv('lags_12months_features.csv', index=False)
#
# #  滞后变量的特征重要性
# # load data
# dataframe = read_csv('lags_12months_features.csv', header=0)
# array = dataframe.values
# # split into input and output
# X = array[:,0:-1]
# y = array[:,-1]
# # fit random forest model
# model = RandomForestRegressor(n_estimators=500, random_state=1)
# model.fit(X, y)
# # show importance scores
# # [ 0.21642244  0.06271259  0.05662302  0.05543768  0.07155573  0.08478599
# # 0.07699371  0.05366735  0.1033234   0.04897883  0.1066669   0.06283236]
# print(model.feature_importances_)
# # plot importance scores
# names = dataframe.columns.values[0:-1]
# ticks = [i for i in range(len(names))]
# pyplot.bar(ticks, model.feature_importances_)
# pyplot.xticks(ticks, names)
# pyplot.show()
#
# # 滞后变量的特征选择
# # load dataset
# dataframe = read_csv('lags_12months_features.csv', header=0)
# # separate into input and output variables
# array = dataframe.values
# X = array[:,0:-1]
# y = array[:,-1]
# # perform feature selection
# rfe = RFE(RandomForestRegressor(n_estimators=500, random_state=1), 3)
# fit = rfe.fit(X, y)
# # report selected features
# print('Selected Features:')
# names = dataframe.columns.values[0:-1]
# for i in range(len(fit.support_)):
#     if fit.support_[i]:
#         print(names[i])
# # plot feature rank
# names = dataframe.columns.values[0:-1]
# ticks = [i for i in range(len(names))]
# pyplot.bar(ticks, fit.ranking_)
# pyplot.xticks(ticks, names)
# pyplot.show()

# model = ARMA(differenced, order=(1, 1))
# result_arma = model.fit( disp=-1, method='css')
# print result_arma

# (839.5188068305007, 845.54080638619814, 841.84756270444905)
# arma_mod30 = sm.tsa.ARMA(differenced,(0,1)).fit()
# print(arma_mod30.aic,arma_mod30.bic,arma_mod30.hqic)

a = sm.tsa.arma_order_select_ic(differenced, ic='aic')['aic_min_order']  # AIC
# b = sm.tsa.arma_order_select_ic(differenced, ic='bic')['bic_min_order']
# c = sm.tsa.arma_order_select_ic(differenced, ic='hqic')['hqic_min_order']
#
# print a
# print b
# print c
# (0, 4)
# (1, 0)
# (1, 0)
series = np.array(series, dtype=np.float)
order = a
train = series[:-3]
test = series[-3:]
tempModel = sm.tsa.ARMA(train, order).fit()
# print tempModel
print tempModel.forecast(3)
