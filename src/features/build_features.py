import pandas as pd
import datetime as dt

def get_datetime_features(dataframe, date_column): 
    dataframe[date_column] = pd.to_datetime(dataframe[date_column])
    dataframe['date'] = dataframe[date_column].dt.date
    dataframe['year'] = dataframe[date_column].dt.year
    #dataframe['year_month'] = dataframe[date_column].dt.to_period('M')
    #dataframe['month_day'] = dataframe[date_column].apply(lambda x: x.strftime("%m-%d") if pd.notnull(x) else '')
    dataframe['month'] = dataframe[date_column].dt.month
    dataframe['month_name'] = dataframe[date_column].dt.month_name()
    dataframe['day'] = dataframe[date_column].dt.day
    dataframe['week'] = dataframe[date_column].dt.isocalendar().week.astype(int)
    dataframe['day_of_week'] = dataframe[date_column].dt.dayofweek + 1
    dataframe['day_of_week_name'] = dataframe[date_column].dt.day_name()
    dataframe['is_weekend'] = (dataframe['day_of_week'] // 5 != 1).astype(int)
    dataframe['time'] = dataframe[date_column].dt.time
    dataframe['hour'] = dataframe[date_column].dt.hour
    dataframe['minute'] = dataframe[date_column].dt.minute
    dataframe['second'] = dataframe[date_column].dt.second
    return dataframe
