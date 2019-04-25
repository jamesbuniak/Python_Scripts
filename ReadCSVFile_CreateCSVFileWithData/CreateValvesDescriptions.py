import os
import csv

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
b=0
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
count = ""

#open file and count the lines
with open('CSV_Valves.csv', 'r', newline='') as csvfile:
    count = sum(1 for row in csvfile)
    print(str(count) + " lines in original file.")
#open original CSV file(two columns)
with open('CSV_Valves.csv', 'r', newline='') as csvfile:
    readFile = csv.reader(csvfile)

#Start FOR
#loop through each row and move to list
    for row in readFile:
        for b in range(0,3):
            if b==0:
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

            #Position0
            position0.append(Column[0])
            position0.append(Column[1])
            position0.append(Column[2])        
            position0.append("Valve$N" + Column[3] + "$N Manual ON")
            position0.append(Column[4])
            position0.append(Column[5] + "," + str(b) + "].0")
            position0.append(Column[6])        
            newFileInfoLine0.append(position0)
            y=y+1

            #Position1
            position1.append(Column[0])
            position1.append(Column[1])
            position1.append(Column[2])        
            position1.append("Valve$N" + Column[3] + "$N Manual OFF")
            position1.append(Column[4])
            position1.append(Column[5] + "," + str(b) + "].1")
            position1.append(Column[6])           
            newFileInfoLine1.append(position1)
            y=y+1

            #Position2
            position2.append(Column[0])
            position2.append(Column[1])
            position2.append(Column[2])        
            position2.append("Valve$N" + Column[3] + "$N Valve Auto")
            position2.append(Column[4])
            position2.append(Column[5] + "," + str(b) + "].2")
            position2.append(Column[6])   
            newFileInfoLine2.append(position2)
            y=y+1

            #Position3
            position3.append(Column[0])
            position3.append(Column[1])
            position3.append(Column[2])        
            position3.append("Valve$N" + Column[3] + "$N InterLock")
            position3.append(Column[4])
            position3.append(Column[5] + "," + str(b) + "].3")
            position3.append(Column[6])  
            newFileInfoLine3.append(position3)
            y=y+1

            #Position4
            position4.append(Column[0])
            position4.append(Column[1])
            position4.append(Column[2])        
            position4.append("Valve$N" + Column[3] + "$N SafetyLock")
            position4.append(Column[4])
            position4.append(Column[5] + "," + str(b) + "].4")
            position4.append(Column[6])  
            newFileInfoLine4.append(position4)
            y=y+1

            #Position5
            position5.append(Column[0])
            position5.append(Column[1])
            position5.append(Column[2])        
            position5.append("Valve$N" + Column[3] + "$N Spare")
            position5.append(Column[4])
            position5.append(Column[5] + "," + str(b) + "].5")
            position5.append(Column[6])  
            newFileInfoLine5.append(position5)
            y=y+1          

            #Position6
            position6.append(Column[0])
            position6.append(Column[1])
            position6.append(Column[2])        
            position6.append("Valve$N" + Column[3] + "$N Spare")
            position6.append(Column[4])
            position6.append(Column[5] + "," + str(b) + "].6")
            position6.append(Column[6]) 
            newFileInfoLine6.append(position6)
            y=y+1

            #Position7
            position7.append(Column[0])
            position7.append(Column[1])
            position7.append(Column[2])        
            if b==0:
                position7.append("Valve$N" + Column[3] + "$N Spare")
            if b==1:
                position7.append("Valve$N" + Column[3] + "$N Lower Seat Active")
            if b==2:
                position7.append("Valve$N" + Column[3] + "$N Upper Seat Active")                 
            position7.append(Column[4])
            position7.append(Column[5] + "," + str(b) + "].7")
            position7.append(Column[6]) 
            newFileInfoLine7.append(position7)
            y=y+1

            #Position8
            position8.append(Column[0])
            position8.append(Column[1])
            position8.append(Column[2])        
            position8.append("Valve$N" + Column[3] + "$N Spare")
            position8.append(Column[4])
            position8.append(Column[5] + "," + str(b) + "].8")        
            position8.append(Column[6]) 
            newFileInfoLine8.append(position8)
            y=y+1

            #Position9
            position9.append(Column[0])
            position9.append(Column[1])
            position9.append(Column[2])        
            position9.append("Valve$N" + Column[3] + "$N Spare")
            position9.append(Column[4])
            position9.append(Column[5] + "," + str(b) + "].9")
            position9.append(Column[6]) 
            newFileInfoLine9.append(position9)
            y=y+1

            #Position10
            position10.append(Column[0])
            position10.append(Column[1])
            position10.append(Column[2])
            if b==0:
                position10.append("Valve$N" + Column[3] + "$N Output")
            if b==1:
                position10.append("Valve$N" + Column[3] + "$N Lower Seat Output")
            if b==2:
                position10.append("Valve$N" + Column[3] + "$N Upper Seat Output")
            position10.append(Column[4])
            position10.append(Column[5] + "," + str(b) + "].10")
            position10.append(Column[6]) 
            newFileInfoLine10.append(position10)
            y=y+1  
            
            #Position11
            position11.append(Column[0])
            position11.append(Column[1])
            position11.append(Column[2])        
            if b==0:
                position11.append("Valve$N" + Column[3] + "$N Opened")
            if b==1:
                position11.append("Valve$N" + Column[3] + "$N Lifted")
            if b==2:
                position11.append("Valve$N" + Column[3] + "$N Lifted")    
            position11.append(Column[4])
            position11.append(Column[5] + "," + str(b) + "].11")
            position11.append(Column[6]) 
            newFileInfoLine11.append(position11)
            y=y+1  
            
            #Position12
            position12.append(Column[0])
            position12.append(Column[1])
            position12.append(Column[2])
            if b==0:
                position12.append("Valve$N" + Column[3] + "$N Closed")
            if b==1:
                position12.append("Valve$N" + Column[3] + "$N Is Not Lifted")
            if b==2:
                position12.append("Valve$N" + Column[3] + "$N Is Not Lifted")                
            position12.append(Column[4])
            position12.append(Column[5] + "," + str(b) + "].12")
            position12.append(Column[6]) 
            newFileInfoLine12.append(position12)
            y=y+1  

            #Position13
            position13.append(Column[0])
            position13.append(Column[1])
            position13.append(Column[2])        
            if b==0:
                position13.append("Valve$N" + Column[3] + "$N Not Opening Alarm")
            if b==1:
                position13.append("Valve$N" + Column[3] + "$N Lower Seat Not Lifting Alarm")
            if b==2:
                position13.append("Valve$N" + Column[3] + "$N Upper Seat Not Lifting Alarm")    
            position13.append(Column[4])
            position13.append(Column[5] + "," + str(b) + "].13")
            position13.append(Column[6]) 
            newFileInfoLine13.append(position13)
            y=y+1

            #Position14
            position14.append(Column[0])
            position14.append(Column[1])
            position14.append(Column[2])        
            if b==0:
                position14.append("Valve$N" + Column[3] + "$N Not Closing Alarm")
            if b==1:
                position14.append("Valve$N" + Column[3] + "$N Lower Lift Off Alarm")
            if b==2:
                position14.append("Valve$N" + Column[3] + "$N Upper Lift Off Alarm")                
            position14.append(Column[4])
            position14.append(Column[5] + "," + str(b) + "].14")
            position14.append(Column[6]) 
            newFileInfoLine14.append(position14)
            y=y+1          

            #Position15
            position15.append(Column[0])
            position15.append(Column[1])
            position15.append(Column[2])        
            position15.append("Valve$N" + Column[3] + "$N Spare")
            position15.append(Column[4])
            position15.append(Column[5] + "," + str(b) + "].15")
            position15.append(Column[6]) 
            newFileInfoLine15.append(position15)
            y=y+1          
          
            with open('CSV_EditedValves.csv', 'a', newline='') as csvfiles:
                tagDescription = csv.writer(csvfiles) 	
    #write each line in new csv row
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
    #Only write name if its first pass on variable
            b=b+1
            if b==3:
                i=i+1
                b=0

##END FOR

print(str(y) + " descriptions created.")
input('Press Enter to Close')



