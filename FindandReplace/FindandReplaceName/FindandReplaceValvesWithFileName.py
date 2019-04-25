import os
import re
folderLocation = 'C:\\PythonScripts\\FindandReplace\\FindandReplaceName\\Example'
i = 0
for root, dirs, files in os.walk(folderLocation): 
    for file in files:
        fname, ext = os.path.splitext(file)
        fnamenumber =  re.findall(r'\d+',fname)
        if ext == '.L5X':
            i+=1
            fullpath = os.path.join(root, file)
            with open(fullpath) as f:
                s = f.read()
                searchstring = 'Routine Use="Target" Name="XVCW_' + fnamenumber[0] + '_XV'
                newstring = 'Routine Use="Target" Name="' + fname 
            s = s.replace(searchstring, newstring)
            with open(fullpath, "w") as f:
                f.write(s)