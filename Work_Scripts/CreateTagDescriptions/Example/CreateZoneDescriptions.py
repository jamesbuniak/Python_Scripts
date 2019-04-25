import os
import csv

#open original CSV file(two columns)
with open('CSV_Zones.csv', 'r', newline='') as csvfile:
    readFile = csv.reader(csvfile)

#create variables
    i=0
    y=0
    newFileInfoLineName = []
    newFileInfoLine0 = []
    newFileInfoLine1 = []
    newFileInfoLine2 = []
    newFileInfoLine3 = []
    newFileInfoLine4 = []
    newFileInfoLine5 = []
    newFileInfoLine6 = []
    newFileInfoLine7 = []
    newFileInfoLine8 = []
    newFileInfoLine9 = []
    newFileInfoLine10 = []
    newFileInfoLine11 = []
    newFileInfoLine12 = []
    newFileInfoLine13 = []
    newFileInfoLine14 = []
    newFileInfoLine15 = [] 
    listCombined = []
    newLineInfo = []
    newLine = []
    positionName = []    
    position0 = []
    position1 = []
    position2 = []
    position3 = []
    position4 = []
    position5 = []
    position6 = []
    position7 = []
    position8 = []
    position9 = []
    position10 = []
    position11 = []
    position12 = []
    position13 = []
    position14 = []
    position15 = []   
    rowArray = []
    Column = []

#Start FOR
#loop through each row and move to list
    for row in readFile:
        newLineInfo = csv.reader(row)
        newLine = list(newLineInfo)

#populate array
        Column.append("COMMENT") #Type
        Column.append("")  #Scope
        Column.append("")  #Name
        Column.append((str(newLine[0]).replace("['","")).replace("']", "")) #Description
        Column.append("") #Data Type
        Column.append((str(newLine[1]).replace("['","")).replace("']", ""))  #Specifier
        Column.append("")  #Attributes

#edit each list item to needed        

        #PositionName
        positionName.append(Column[0])
        positionName.append(Column[1])
        positionName.append(Column[2])        
        positionName.append(Column[3] + " Zone")
        positionName.append(Column[4])
        positionName.append(Column[5])
        positionName.append(Column[6])        
        newFileInfoLineName.append(positionName)
        y=y+1

        #Position0
        position0.append(Column[0])
        position0.append(Column[1])
        position0.append(Column[2])        
        position0.append(Column[3] + " In Alarm")
        position0.append(Column[4])
        position0.append(Column[5] + ".0")
        position0.append(Column[6])        
        newFileInfoLine0.append(position0)
        y=y+1

        #Position1
        position1.append(Column[0])
        position1.append(Column[1])
        position1.append(Column[2])        
        position1.append(Column[3] + " In Manual")
        position1.append(Column[4])
        position1.append(Column[5] + ".1")
        position1.append(Column[6])           
        newFileInfoLine1.append(position1)
        y=y+1
      
        with open('CSV_EditedZones.csv', 'a', newline='') as csvfiles:
            tagDescription = csv.writer(csvfiles) 	
#write each line in new csv row
            tagDescription.writerow(newFileInfoLineName[i])
            tagDescription.writerow(newFileInfoLine0[i])
            tagDescription.writerow(newFileInfoLine1[i])

#clear the arrays used
        positionName.clear()
        position0.clear()
        position1.clear()
       
        Column.clear()
        
#increment the count
        i=i+1

##END FOR

print(str(y) + " descriptions created.")
input('Press Enter to Close')



