import os
import csv

#open original CSV file(two columns)
with open('CSV_ValveAlarms.csv', 'r', newline='') as csvfile:
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
        positionName.append("ValveAlarm$N" + Column[3] + "$N Valve Alarm")
        positionName.append(Column[4])
        positionName.append(Column[5])
        positionName.append(Column[6])        
        newFileInfoLineName.append(positionName)
        y=y+1

        #Position0
        position0.append(Column[0])
        position0.append(Column[1])
        position0.append(Column[2])        
        position0.append("ValveAlarm$N" + Column[3] + "$N Not Closing")
        position0.append(Column[4])
        position0.append(Column[5] + ".0")
        position0.append(Column[6])        
        newFileInfoLine0.append(position0)
        y=y+1

        #Position1
        position1.append(Column[0])
        position1.append(Column[1])
        position1.append(Column[2])        
        position1.append("ValveAlarm$N" + Column[3] + "$N Not Opening")
        position1.append(Column[4])
        position1.append(Column[5] + ".1")
        position1.append(Column[6])           
        newFileInfoLine1.append(position1)
        y=y+1

        #Position2
        position2.append(Column[0])
        position2.append(Column[1])
        position2.append(Column[2])        
        position2.append("ValveAlarm$N" + Column[3] + "$N Lower Seat Not Lifting")
        position2.append(Column[4])
        position2.append(Column[5] + ".2")
        position2.append(Column[6])   
        newFileInfoLine2.append(position2)
        y=y+1

        #Position3
        position3.append(Column[0])
        position3.append(Column[1])
        position3.append(Column[2])        
        position3.append("ValveAlarm$N" + Column[3] + "$N Upper Seat Not Lifting")
        position3.append(Column[4])
        position3.append(Column[5] + ".3")
        position3.append(Column[6])  
        newFileInfoLine3.append(position3)
        y=y+1

        #Position4
        position4.append(Column[0])
        position4.append(Column[1])
        position4.append(Column[2])        
        position4.append("ValveAlarm$N" + Column[3] + "$N CheckSum Error")
        position4.append(Column[4])
        position4.append(Column[5] + ".4")
        position4.append(Column[6])  
        newFileInfoLine4.append(position4)
        y=y+1

        #Position5
        position5.append(Column[0])
        position5.append(Column[1])
        position5.append(Column[2])        
        position5.append("ValveAlarm$N" + Column[3] + "$N Position Overrange")
        position5.append(Column[4])
        position5.append(Column[5] + ".5")
        position5.append(Column[6])  
        newFileInfoLine5.append(position5)
        y=y+1          

        #Position6
        position6.append(Column[0])
        position6.append(Column[1])
        position6.append(Column[2])        
        position6.append("ValveAlarm$N" + Column[3] + "$N No DeviceNet")
        position6.append(Column[4])
        position6.append(Column[5] + ".6")
        position6.append(Column[6]) 
        newFileInfoLine6.append(position6)
        y=y+1

        #Position7
        position7.append(Column[0])
        position7.append(Column[1])
        position7.append(Column[2])        
        position7.append("ValveAlarm$N" + Column[3] + "$N TX RX Error")
        position7.append(Column[4])
        position7.append(Column[5] + ".7")
        position7.append(Column[6]) 
        newFileInfoLine7.append(position7)
        y=y+1

        #Position8
        position8.append(Column[0])
        position8.append(Column[1])
        position8.append(Column[2])        
        position8.append("ValveAlarm$N" + Column[3] + "$N Button 1 Failure")
        position8.append(Column[4])
        position8.append(Column[5] + ".8")        
        position8.append(Column[6]) 
        newFileInfoLine8.append(position8)
        y=y+1

        #Position9
        position9.append(Column[0])
        position9.append(Column[1])
        position9.append(Column[2])        
        position9.append("ValveAlarm$N" + Column[3] + "$N Button 2 Failure")
        position9.append(Column[4])
        position9.append(Column[5] + ".9")
        position9.append(Column[6]) 
        newFileInfoLine9.append(position9)
        y=y+1

        #Position10
        position10.append(Column[0])
        position10.append(Column[1])
        position10.append(Column[2])        
        position10.append("ValveAlarm$N" + Column[3] + "$N Actuation Timeout")
        position10.append(Column[4])
        position10.append(Column[5] + ".10")
        position10.append(Column[6]) 
        newFileInfoLine10.append(position10)
        y=y+1  
        
        #Position11
        position11.append(Column[0])
        position11.append(Column[1])
        position11.append(Column[2])        
        position11.append("ValveAlarm$N" + Column[3] + "$N Multiple Solenoid ON")
        position11.append(Column[4])
        position11.append(Column[5] + ".11")
        position11.append(Column[6]) 
        newFileInfoLine11.append(position11)
        y=y+1  
        
        #Position12
        position12.append(Column[0])
        position12.append(Column[1])
        position12.append(Column[2])        
        position12.append("ValveAlarm$N" + Column[3] + "$N Spare")
        position12.append(Column[4])
        position12.append(Column[5] + ".12")
        position12.append(Column[6]) 
        newFileInfoLine12.append(position12)
        y=y+1  

        #Position13
        position13.append(Column[0])
        position13.append(Column[1])
        position13.append(Column[2])        
        position13.append("ValveAlarm$N" + Column[3] + "$N Spare")
        position13.append(Column[4])
        position13.append(Column[5] + ".13")
        position13.append(Column[6]) 
        newFileInfoLine13.append(position13)
        y=y+1

        #Position14
        position14.append(Column[0])
        position14.append(Column[1])
        position14.append(Column[2])        
        position14.append("ValveAlarm$N" + Column[3] + "$N Spare")
        position14.append(Column[4])
        position14.append(Column[5] + ".14")
        position14.append(Column[6]) 
        newFileInfoLine14.append(position14)
        y=y+1          

        #Position15
        position15.append(Column[0])
        position15.append(Column[1])
        position15.append(Column[2])        
        position15.append("ValveAlarm$N" + Column[3] + "$N Spare")
        position15.append(Column[4])
        position15.append(Column[5] + ".15")
        position15.append(Column[6]) 
        newFileInfoLine15.append(position15)
        y=y+1          
      
        with open('CSV_EditedValveAlarms.csv', 'a', newline='') as csvfiles:
            tagDescription = csv.writer(csvfiles) 	
#write each line in new csv row
            tagDescription.writerow(newFileInfoLineName[i])
            tagDescription.writerow(newFileInfoLine0[i])
            tagDescription.writerow(newFileInfoLine1[i])
            tagDescription.writerow(newFileInfoLine2[i])
            tagDescription.writerow(newFileInfoLine3[i])
            tagDescription.writerow(newFileInfoLine4[i])
            tagDescription.writerow(newFileInfoLine5[i])
            tagDescription.writerow(newFileInfoLine6[i])
            tagDescription.writerow(newFileInfoLine7[i])
            tagDescription.writerow(newFileInfoLine8[i])
            tagDescription.writerow(newFileInfoLine9[i])
            tagDescription.writerow(newFileInfoLine10[i])
            tagDescription.writerow(newFileInfoLine11[i])
            tagDescription.writerow(newFileInfoLine12[i])
            tagDescription.writerow(newFileInfoLine13[i])
            tagDescription.writerow(newFileInfoLine14[i])
            tagDescription.writerow(newFileInfoLine15[i])            
            
#clear the arrays used
        positionName.clear()
        position0.clear()
        position1.clear()
        position2.clear()
        position3.clear()
        position4.clear()
        position5.clear()
        position6.clear()
        position7.clear()
        position8.clear()
        position9.clear()
        position10.clear()
        position11.clear()
        position12.clear()
        position13.clear()
        position14.clear()
        position15.clear()         
        Column.clear()
        
#increment the count
        i=i+1

##END FOR

print(str(y) + " descriptions created.")
input('Press Enter to Close')



