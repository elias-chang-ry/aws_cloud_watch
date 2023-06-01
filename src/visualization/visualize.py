import pandas as pd
import datetime as dt
import numpy as np

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
from statsmodels.tsa.seasonal import seasonal_decompose

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="ticks", color_codes=True)

import sys


def plot_histogram_custom_bins(dataframe, data, histogram_bins, x_label, y_label, title):
    plt = dataframe[data].hist(bins = histogram_bins)
    plt.set_xlabel(x_label)
    plt.set_ylabel(y_label)
    plt.set_title(title);
    
def plot_bar(dataframe, data, sort, x_label, y_label, title):
    data = dataframe[data].value_counts(sort = sort)
    plt = data.plot.bar(xlabel = x_label, ylabel = y_label
                                                     , title = title, rot = 0);
    for index, data in enumerate(data):
        plt.text(x = index, y = data + 1, s = f"{data}", ha = 'center', va = 'bottom', fontweight = 'bold');

def groupby_filter(dataframe, filter_by, filter_value, groupby, measure_by, ylabel, title, rot):
    data = dataframe[(dataframe[filter_by] == filter_value)].groupby([groupby]).agg({measure_by: ['min', 'max', 'mean']})
    plt = data.plot.line(ylabel = ylabel, title = title, rot = rot)
    plt.legend(['min', 'max', 'mean'], title = title);

def two_groupby_filter(dataframe, filter_by, filter_value, groupby_a, groupby_b, measure_by, measurement, ylabel, title, rot):
    data = dataframe[(dataframe[filter_by] == filter_value)].groupby([groupby_a, groupby_b]).agg({measure_by: [measurement]})
    plt = data.unstack().plot.line(ylabel = ylabel, title = title, rot = rot);
    plt.legend(['24ae8d', '53ea38', '5f5533', 'fe7f93'], title = 'AIM');

def plot_line_index(dataframe, x_value, y_value, title, legend_title):
    sns.set(rc={'figure.figsize':(20,5)})
    dataframe.reset_index().plot(x = x_value, y = y_value, title = title)
    plt.legend([legend_title])
    sns.reset_orig();

def plot_line_filter(dataframe, filter_by, filter_value, x_value, y_value, title, legend_title):
    sns.set(rc={'figure.figsize':(20,5)})
    data = dataframe[(dataframe[filter_by] == filter_value)]
    plt = data.plot.line(x = x_value, y = y_value, rot = 0, title = title)
    plt.legend([legend_title])
    sns.reset_orig()

def plot_boxplot(dataframe, filter_by, filter_value, x_value, y_value, x_label, y_label, sub_title_1, sub_title_2):
    data = dataframe[(dataframe[filter_by] == filter_value)]
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    fig.suptitle('Boxplot of ' + y_label + ' of ' + filter_value)

    ax=axes[0]
    sns.boxplot(ax=axes[0], x = data[x_value], y  = data[y_value], showfliers = True)
    axes[0].set_title(sub_title_1)
    axes[0].set_xlabel(x_label)
    axes[0].set_ylabel(y_label)
    axes[0].set_xticklabels(axes[0].get_xticklabels(),rotation=45)

    sns.boxplot(ax=axes[1], x = data[x_value], y  = data[y_value], showfliers = False)
    axes[1].set_title(sub_title_2)
    axes[1].set_xlabel(x_label)
    axes[1].set_ylabel(y_label)
    axes[1].set_xticklabels(axes[1].get_xticklabels(),rotation=45);

def plot_test_stationarity(timeseries, test_on):
    
    sns.set(rc={'figure.figsize':(20,5)})

    #Determing rolling statistics
    rolmean = timeseries.rolling(12).mean()
    rolstd = timeseries.rolling(12).std()

    #Plot rolling statistics:
    orig = plt.plot(timeseries[test_on], color='blue',label='Original')
    mean = plt.plot(rolmean[test_on], color='red', label='Rolling Mean')
    std = plt.plot(rolstd[test_on], color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    sns.reset_orig();
    
    #Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries.iloc[:,0].values, autolag='AIC')
    SignificanceLevel=dftest[4].get('5%')
    pValue = dftest[1]
    if (pValue<SignificanceLevel):
        isStationary = True
    else:
        isStationary = False
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)
    print("Is the time series stationary? " + str(isStationary))


def plot_decompose(timeseries, test_on, model):
    result = seasonal_decompose(timeseries[test_on], model = model)
    sns.set(rc={'figure.figsize':(20,10)})
    result.plot()
    plt.show()
    sns.reset_orig();

def plot_train_valid(timeseries, timeseries_name, test_on, train_size):
    #divide into train and validation set
    train = timeseries[:int(train_size*(len(timeseries[test_on])))]
    valid = timeseries[int(train_size*(len(timeseries[test_on]))):]

    #preprocessing (since arima takes univariate series as input)
    train = train[[test_on]]
    valid = valid[[test_on]]

    #plotting the data
    sns.set(rc={'figure.figsize':(20,10)})
    train[test_on].plot()
    valid[test_on].plot()
    plt.title('Train & valid split of cpu_utilization of ' + timeseries_name)
    sns.reset_orig()
