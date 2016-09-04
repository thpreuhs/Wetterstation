
import pandas as pd
import HelpFunctions as hf
import numpy as np
import matplotlib.pyplot as plt


filename = r'davis-2016-08.txt'
filename_out = r'davis-2016-08.csv'
wetter_data = hf.read_wetter_export(filename, True)

###get wether data from 01.08.16
wetter_data.to_csv(filename_out)

a = 10
