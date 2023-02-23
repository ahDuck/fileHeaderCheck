import pandas as pd
import os
import glob
import csv

path = 'C:/Users/ahouck/OneDrive - Aegis Premier Technologies/Documents/headerTesting' #set file path
extension = 'csv'   #set file extension - the files that will be
os.chdir(path)  #change directory
result = glob.glob('*.{}'.format(extension))    #result is a list of the file names of specified extension/file type in specified directory
# print(type(result))

dfDict = {} #create an empty dictionary                                                                         

for i in result:   #iterate over files in result
    df = pd.read_csv(str(i))    #create data frame for each iteration
    imported_header = tuple(df.axes[1].values)  #assign imported_header to the tuple of the data frame header
    #print(imported_header)
    if imported_header not in dfDict.values():  #if the header does not already exist in the dictionary
        dfDict[i] = imported_header #add to the dictionary a key value pair of the file name and the header
    else:   #if the does already exist in the dictionary
        matchedKey = [x for x in dfDict if dfDict[x]==imported_header]  #determine the key for which the header values match
        #print(dfDict[matchedKey[0]])
        dfDict[matchedKey[0]+ ', ' + str(i)] = dfDict.pop(matchedKey[0])    #update the key for which the header values match with a new key, now including the newest file name
print(dfDict)

#dfDict.to_excel("output2.xlsx")

df1 = pd.DataFrame.from_dict(dfDict, orient='index')
print(df1)
df1.to_excel("output2.xlsx")