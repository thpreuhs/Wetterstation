import HelpFunctions as hf
import os

data = os.getcwd()+r'\Data'
data_raw = os.getcwd()+r'\Data\Raw'
data_converted = os.getcwd()+r'\Data\Converted'

for filename in os.listdir(data):
    if filename.endswith(".txt"):
        file = hf.read_wetter_export(data+'\\'+filename,True)
        file.to_csv(data_converted+'\\' +filename[0:-3] + 'cvs',low_memory=False)
        os.rename(data+'\\'+filename, data_raw +'\\'+ filename)

