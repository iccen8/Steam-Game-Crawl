import pandas as pd

df = pd.read_csv('tableA.csv')

minLenName = df['Name'].str.len().min()
maxLenName = df['Name'].str.len().max()
aveLenName = df['Name'].str.len().mean()

minLenPublisher = df['Publisher'].str.len().min()
maxLenPublisher = df['Publisher'].str.len().max()
aveLenPublisher = df['Publisher'].str.len().mean()

minLenDeveloper = df['Developer'].str.len().min()
maxLenDeveloper = df['Developer'].str.len().max()
aveLenDeveloper = df['Developer'].str.len().mean()



print "Name: %d, %d, %f" %(minLenName, maxLenName, aveLenName)
print "Publisher: %d, %d, %f" %(minLenPublisher, maxLenPublisher, aveLenPublisher )
print "Developer: %d, %d, %f" %(minLenDeveloper, maxLenDeveloper, aveLenDeveloper) 

