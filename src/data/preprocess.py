import pandas as pd
import glob, os

def read_multiple_files_with_filename(file_path, name_preflix, file_type, datetime_column):
    """Read multiple files from the file path defined, add the file name as a column
    , convert specified column to datetime and return the dataframe

    Args:
        file_path ([string]): [file path of files]
        name_preflix ([string]): [preflix of file use for analysis]
        file_type ([string]): [file type of files]
        datetime_column ([string]): [datetime column]

    Returns:
        [dataframe]: [a concatination of all files in the specified folder with file
        name as a column]
    """
    all_filenames = [i for i in glob.glob(file_path + name_preflix + '*.' + file_type)]
    dataframe = pd.concat([pd.read_csv(fp, parse_dates=['timestamp']).assign(aim
    = os.path.basename(fp).replace(name_preflix, '').split('.')[0]) for fp in all_filenames])
    return dataframe
