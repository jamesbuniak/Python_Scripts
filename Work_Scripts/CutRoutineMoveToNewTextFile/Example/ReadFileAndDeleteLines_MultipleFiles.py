import os, re

lineFound = False
folderLocation = 'C:\\PythonScripts\\CombineRoutines\\CutRoutineMoveToNewTextFile\\Example\\'

for root, dirs, files in os.walk(folderLocation):
    for file in files:
        fname, ext = os.path.splitext(file)
        with open((fname + ext), "r") as input:
            with open("NewFile.txt", "a") as output: 
                for line in input:
                    if lineFound or line=='<Routines Use="Context">'+"\n":
                        if lineFound==True:
                            output.write(line)
                            print(line)
                        if line=='</Routine>'+'\n':
                            lineFound=False
                        if line=='<Routines Use="Context">'+'\n':
                            lineFound=True