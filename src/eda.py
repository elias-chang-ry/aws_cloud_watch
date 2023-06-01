import pandas as pd

def get_shape(dataframe):
    print("No. of features:", dataframe.shape[1])
    print("No. of observations:", dataframe.shape[0])

def find_duplicates(dataframe):
    """Prints the number & percentage of duplicates of each column if there there are duplicates
    , if not the function will print out 'No duplicates in ths dataframe'

    Args:
        dataframe (dataframe]): [dataframe used for the analysis]
    """
    if len(dataframe[dataframe.duplicated()]) == 0:
        print('No duplicates in ths dataframe')
    else:
        padding = 0

        for (columnName, columnData) in dataframe.iteritems():
            if len(columnName) > padding:
                padding = len(columnName)

        padding_bigger = padding - len('Column Name') + 1
        padding_smaller = 0

        print('Column name' + (' ' * (padding - len('Column Name') + 1) if padding > len('Column Name') else '\t')
            + 'No. of missing values\t' + '% of missing values')
        for (columnName, columnData) in dataframe.iteritems():
            if columnData.isnull().sum() >= 1:
                # After the : sign, take the padding and minus the number of characters and plus, to get a evenly distributed column
                t = columnName + (' ' * (padding - len(columnName) + 1)) + str(columnData.isnull().sum())
                # Use the len of "No. of missing values", the column name to pad the columns to get a evenly distributed column
                t = t + " " * (len("No. of missing values") - len(str(columnData.isnull().sum())))
                t = t + '\t' + str(round(columnData.isnull().sum() * 100 / len(dataframe),2))
                print(t)
        
        dataframe[dataframe.duplicated()]

def find_uniques(dataframe):
    """Prints the number of unique data of each columnand list the unique if the unique value
    if it is less than or equal to 50 or it will print the lowest & highest values

    Args:
        dataframe (dataframe]): [dataframe used for the analysis]
    """
    padding_column_data = 1
    padding_column_name = len('No. of unique values')

    for (columnName, columnData) in dataframe.iteritems():
        column_name = dataframe[columnName].unique()
        if dataframe[columnName].dtype != 'object':
            column_name.sort()
        print('Colunm Name:' + ' ' * (padding_column_name - len('Colunm Name:') + 1), columnName)
        print('No. of unique values:', columnData.nunique())
        print('Values:')
        print(column_name if columnData.nunique() <= 50 else str(min(columnData)) + ' - ' + str(max(columnData)))
        print('-' * 80)
