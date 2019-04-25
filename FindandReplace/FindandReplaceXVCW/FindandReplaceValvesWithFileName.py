import os
import re
search_string = 'XVCW['
folderLocation = 'C:\\PythonScripts\\FindandReplace\\Example'
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
            s = s.replace(search_string, search_string + fnamenumber[0])
            with open(full_path, "w") as f:
                f.write(s)