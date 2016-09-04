import numpy as np
from matplotlib.pyplot import *



def generate_Data():
    filename = r'download-2016-07-28.txt'

    with open(filename, 'r') as f:
        first_line = f.readline()
        Second_line = f.readline()
        Third_line = f.readline()
        wind_dir_vec = np.zeros(17)
        num_entrys = 0
        for line in f:
            num_entrys +=1
            line_array = line.split()
            wind_dir = wtoi(line_array[8])
            wind_speed = float(line_array[7])
            wind_dir_vec[wind_dir] += wind_speed
            wind_run = line_array[9]
            if(wind_dir == 16):
                wind_dir_vec[16] +=1
            elif(wind_speed == 0):
                wind_dir_vec[16] +=1
        wind_dir_vec /= num_entrys-wind_dir_vec[16]
    return wind_dir_vec

#def itoA(i):
#    return i*22.5

def wtoi(wd):
    if wd == 'N':
        return 0
    if wd == 'NNE':
        return 1
    if wd == 'NE':
        return 2
    if wd == 'ENE':
        return 3
    if wd == 'E':
        return 4
    if wd == 'ESE':
        return 5
    if wd == 'SE':
        return 6
    if wd == 'SSE':
        return 7
    if wd == 'S':
        return 8
    if wd == 'SSW':
        return 9
    if wd == 'SW':
        return 10
    if wd == 'WSW':
        return 11
    if wd == 'W':
        return 12
    if wd == 'WNW':
        return 13
    if wd == 'NW':
        return 14
    if wd == 'NNW':
        return 15
    if wd == '---':
        return 16




