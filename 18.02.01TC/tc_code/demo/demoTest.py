#-*- coding: UTF-8 -*-

# 如何解释具有高度相关性的滞后观测的相关图。
# 如何计算和查看时间序列数据中的特征重要性得分。
# 如何使用特征选择来确定时间序列数据中最相关的输入变量。

from pandas import Series
from pandas import read_csv
from statsmodels.graphics.tsaplots import plot_acf
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot
from pandas import DataFrame
# 递归特征选择（Recursive Feature Selection，RFE）
# RFE 可以创建预测模型，对特征值赋予不同的权值，并删掉那些权重最小的特征，通过不断重复这一流程，最终就能得到预期数量的特征。
from sklearn.feature_selection import RFE

# 载入数据
# load dataset
# series = Series.from_csv('car-sales.csv', header=0)
# # display first few rows
# print(series.head(5))
# # line plot of dataset
# series.plot()
# pyplot.show()

# 平稳化-季节差分（周期为12）-差分运算成功消除了季节性变化和增长趋势信息
# # seasonal difference
# differenced = series.diff(12)
# # trim off the first year of empty data
# differenced = differenced[12:]
# # save differenced dataset to file
# differenced.to_csv('seasonally_adjusted.csv')
# # plot differenced dataset
# differenced.plot()
# pyplot.show()

# 自相关图-展示了每个滞后观察结果的相关性，以及这些相关性是否具有统计学的显着性
# x 轴：表示滞后值，
# y 轴上 -1 和 1 之间：表现了这些滞后值的正负相关性
# 蓝色区域中的点表示统计学显著性：指原假设为真的情况下拒绝零假设所要承担的风险水平
# series = Series.from_csv('seasonally_adjusted.csv', header=None)
# plot_acf(series.dropna())
# pyplot.show()

# 时间序列到监督学习-这个过程可以在任意的时间步长下重复进行，例如6或24个月，感兴趣的朋友可以自行尝试。
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

#  滞后变量的特征重要性
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

# 滞后变量的特征选择
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


