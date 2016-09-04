import pandas as pd


def read_wetter_export(path, convert_as_timeseries=True):
    file = pd.read_csv(path, sep='\t', header=[0, 1],low_memory=False)

    # get headers as list
    header_list = list(file.columns.values)
    # buffer for new headers
    header_list_new = list()
    # create new headers, where the rows per header column are concatenated
    for header in header_list:
        concatenateA = header[0]
        concatenateB = header[1]
        if "Unnamed:" in concatenateA:
            header_list_new.append(concatenateB)
        elif "Unnamed:" in concatenateB:
            header_list_new.append(concatenateA)
        else:
            header_list_new.append(concatenateA + " " + concatenateB)
    # assign new header to file
    file.columns = header_list_new
    if convert_as_timeseries:
        return convert_to_timeseries(file)
    else:
        return file

def convert_to_timeseries(file):
    tmp_time = file['Date'] + file['Time']
    file['Date_Time'] = pd.to_datetime(tmp_time, format="%d.%m.%y%H:%M")
    file = file.drop(["Date", 'Time'], axis=1)
    return file.set_index('Date_Time', drop=True)