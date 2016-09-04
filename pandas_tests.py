import pandas as pd
import io


filename = r'davis-2016-08.txt'

# read text file, with tab as seperator and first two rows as header
file = pd.read_csv(filename,sep='\t',header=[0,1])
# get headers as list
header_list = list(file.columns.values)
# buffer for new headers
header_list_new = list()
# create new headers, where the rows per header column are concatenated
for header in header_list:
    concatenateA = header[0]
    concatenateB = header[1]
    if "Unnamed:" in concatenateA:
        concatenateA = ""
    if "Unnamed:" in concatenateB:
        concatenateB = ""
    header_list_new.append(concatenateA+" " +concatenateB)
# assign new header to file
file.columns = header_list_new
