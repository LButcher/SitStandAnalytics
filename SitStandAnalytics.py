import pandas as pd

#Goes through a given dataframe and filters out 'noise' values.
    # Noise defined by repeated switching between values or extreme values
def cleanValues(df):
    previousRow = None
    rowsToDrop = []
    for row in df.iterrows():
        oldHeight = row[1][2]
        newHeight = row[1][3]
        currentRow = [oldHeight,newHeight]
        
        if(previousRow!=None):
            #compare the new measured height to the old recorded height of the previous row
            if(abs(row[1][3]-previousRow[1][2])<3):
                if(previousRow[0] not in rowsToDrop):
                    rowsToDrop.append(previousRow[0])
                if(row[0] not in rowsToDrop):
                    rowsToDrop.append(row[0])
            #Check if the height is a reasonable height
            elif(row[1][3] <= 50):
                rowsToDrop.append(row[0])
        
        previousRow = row
    df.drop(rowsToDrop,inplace=True)
    
#Reads CSV into a dataframe
deskReadings = pd.read_csv("http://99.231.14.167/desks",names=[0,1,2,3])

#Grab and store unique IDs for each sensor system
iDs = deskReadings[0].unique()

#Create a dataframe for each ID
dataFrames = {}
for iD in iDs:
    dataFrames[iD] = pd.DataFrame()

#Populate each dataframe with the appropriate data
for desk in dataFrames:
    dataFrames[desk] = deskReadings[deskReadings[0]==desk]

#Clean data in each dataframe
for desk in dataFrames:
    cleanValues(dataFrames[desk])

#Output the cleaned dataframes
print(dataFrames)
    



    
#Export to a CSV file (replace, not append)




