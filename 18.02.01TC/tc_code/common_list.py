#!/usr/bin/env python
# coding:utf8
import csv
from numpy import *
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import operator
from matplotlib.font_manager import FontProperties
import time
import pandas as pd

def draw_bar(labels,quants):
    width = 0.4
    ind = np.linspace(0.5,9.5,10)
    # make a square figure
    fig = plt.figure(1)
    ax  = fig.add_subplot(111)
    # Bar Plot
    ax.bar(ind-width/2,quants,width,color='green')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    # labels
    ax.set_xlabel('Country')
    ax.set_ylabel('GDP (Billion US dollar)')
    # title
    ax.set_title('Top 10 GDP Countries', bbox={'facecolor':'0.8', 'pad':5})
    plt.grid(True)
    plt.show()
    plt.savefig("bar.jpg")
    plt.close()


labels = ['USA', 'China', 'India', 'Japan', 'Germany', 'Russia', 'Brazil', 'UK', 'France', 'Italy']
quants = [15094025.0, 11299967.0, 4457784.0, 4440376.0, 3099080.0, 2383402.0, 2293954.0, 2260803.0, 2217900.0,1846950.0]
draw_bar(labels, quants)