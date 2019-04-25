import os
import re
search_stringBeginning = '<Routine Use="Target" Name="'
search_stringEnd = '" Type="RLL">'
folderLocation = 'C:\\PythonScripts\\FindandReplace\\FindandReplaceName\\Example'
i = 0
for root, dirs, files in os.walk(folderLocation): 
    for file in files:
        fname, ext = os.path.splitext(file)
        fnamenumber = re.findall(r'\d+', fname)
        if ext == '.L5X':
            i+=1
            full_path = os.path.join(root, file)
            with open(full_path) as f:
                s = f.read()
                newname = search_stringBeginning + fname + search_stringEnd
            s = s.replace(r'(?=search_stringBeginning).*(?=search_stringEnd)',newname)
            with open(full_path, "w") as f:
                f.write(s)