import os
import re

lineFound = False
#folderLocation = 'C:\\PythonScripts\\CombineRoutines\\CutRoutineMoveToNewTextFile\\Example\\'

#for root, dirs, files in os.walk(folderLocation):
#    for file in files:
with open('XVCW_195_XV322_08.l5x', "r") as input:
    with open("NewFile.txt", "w") as output: 
        for line in input:
            if lineFound or line=='<Routines Use="Context">'+"\n":
                if lineFound==True:
                    output.write(line)
                if line=='</Routine>'+'\n':
                	lineFound=False
                if line=='<Routines Use="Context">'+'\n':
                    lineFound=True