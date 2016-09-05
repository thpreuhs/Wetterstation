import pandas as pd


def read_wetter_export(path, convert_as_timeseries=True):
    file = pd.read_csv(path, sep='\t', header=[0, 1], low_memory=False)

    # get headers as list
    header_list = list(file.columns.values)
    # buffer for new headers
    header_list_new = list()
    # create new headers, where the rows per header column are concatenated
    for header in header_list:
        concatenateA = header[0].strip()
        concatenateB = header[1].strip()
        if "Unnamed:" in concatenateA:
            header_list_new.append(concatenateB)
        elif "Unnamed:" in concatenateB:
            header_list_new.append(concatenateA)
        else:
            header_list_new.append(concatenateA + " " + concatenateB)
    # assign new header to file
    file.columns = header_list_new
    file['Wind Dir Degree'] = file['Wind Dir'].apply(__wtoi)
    if convert_as_timeseries:
        return convert_to_timeseries(file)
    else:
        return file

def convert_to_timeseries(file):
    tmp_time = file['Date'] + file['Time']
    file['Date_Time'] = pd.to_datetime(tmp_time, format="%d.%m.%y%H:%M")
    file = file.drop(["Date", 'Time'], axis=1)
    return file.set_index('Date_Time', drop=True)


def __wtoi(wd):
    if wd == 'N':
        return 0*22.5
    if wd == 'NNE':
        return 1*22.5
    if wd == 'NE':
        return 2*22.5
    if wd == 'ENE':
        return 3*22.5
    if wd == 'E':
        return 4*22.5
    if wd == 'ESE':
        return 5*22.5
    if wd == 'SE':
        return 6*22.5
    if wd == 'SSE':
        return 7*22.5
    if wd == 'S':
        return 8*22.5
    if wd == 'SSW':
        return 9*22.5
    if wd == 'SW':
        return 10*22.5
    if wd == 'WSW':
        return 11*22.5
    if wd == 'W':
        return 12*22.5
    if wd == 'WNW':
        return 13*22.5
    if wd == 'NW':
        return 14*22.5
    if wd == 'NNW':
        return 15*22.5
    if wd == '---':
        return 16*22.5