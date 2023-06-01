import pandas as pd
import datetime as dt

def get_date(is_true, date_column):
    if is_true == True:
        dataframe['date'] = dataframe[date_column].dt.date
        return dataframe

def get_year(is_true, date_column):
    if is_true == True:
        dataframe['year'] = dataframe[date_column].dt.year
        return dataframe

def get_year_month(is_true, date_column):
    if is_true == True:
        dataframe['year_month'] = dataframe[date_column].dt.to_period('M')
        return dataframe

def get_month_day(is_true, date_column):
    if is_true == True:
        dataframe['month_day'] = dataframe[date_column].apply(lambda x: x.strftime("%m-%d") if pd.notnull(x) else '')
        return dataframe

def get_month(is_true, date_column):
    if is_true == True:
        dataframe['month'] = dataframe[date_column].dt.month
        return dataframe

def get_month_name(is_true, date_column):
    if is_true == True:
        dataframe['month_name'] = dataframe[date_column].dt.month_name()
        return dataframe

def get_day(is_true, date_column):
    if is_true == True:
        dataframe['day'] = dataframe[date_column].dt.day
        return dataframe

def get_week(is_true, date_column):
    if is_true == True:
        dataframe['week'] = dataframe[date_column].dt.isocalendar().week.astype(int)
        return dataframe

def get_day_of_week(is_true, date_column):
    if is_true == True:
        dataframe['day_of_week'] = dataframe[date_column].dt.dayofweek + 1
        return dataframe

def get_day_of_week_name(is_true, date_column):
    if is_true == True:
        dataframe['day_of_week_name'] = dataframe[date_column].dt.day_name()
        return dataframe

def get_is_weekend(is_true, date_column):
    if is_true == True:
        dataframe['is_weekend'] = (dataframe['day_of_week'] // 5 != 1).astype(int)
        return dataframe

def get_time(is_true, date_column):
    if is_true == True:
        dataframe['time'] = dataframe[date_column].dt.time
        return dataframe

def get_hour(is_true, date_column):
    if is_true == True:
        dataframe['hour'] = dataframe[date_column].dt.hour
        return dataframe

def get_minute(is_true, date_column):
    if is_true == True:
        dataframe['minute'] = dataframe[date_column].dt.minute
        return dataframe

def get_second(is_true, date_column): 
    if is_true == True:
        dataframe['second'] = dataframe[date_column].dt.second
        return dataframe

def get_date_features(dataframe, date_column, date_is_true, year_is_true, year_month_is_true, month_day_is_true
, month_is_true, month_name_is_true, day_is_true):
    get_date(date_column, date_is_true)
    get_year(date_column, year_is_true)
    get_year_month(date_column, year_month_is_true)
    get_month_day(date_column, month_day_is_true)
    get_month(date_column, month_is_true)
    get_month_name(date_column, month_name_is_true)
    get_day(date_column, day_is_true)
    return dataframe

def get_calender_features(dataframe, date_column, week_is_true, day_of_week_is_true, day_of_week_name_is_true
, is_weekend_is_true):
    get_week(date_column, week_is_true)
    get_day_of_week(date_column, day_of_week_is_true)
    get_day_of_week_name(date_column, day_of_week_name_is_true)
    get_is_weekend(date_column, is_weekend_is_true)
    return dataframe

def get_time_features(dataframe, date_column, time_is_true, hour_is_true, minute_is_true
, second_is_true):
    get_time(date_column, time_is_true)
    get_hour(date_column, hour_is_true)
    get_minute(date_column, minute_is_true)
    get_second(date_column, second_is_true)
    return dataframe
