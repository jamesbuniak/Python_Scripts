# importing libraries
import os

# defining location of parent folder
BASE_DIRECTORY = 'C:\\PythonScripts\\FindandReplace\\FindandReplaceName\\Example'
output_file = open('A_NewRoutine.txt', 'w')
output = {}
file_list = []

# scanning through sub folders
for (dirpath, dirnames, filenames) in os.walk(BASE_DIRECTORY):
    for f in filenames:
        if 'XVCW' in str(f):
            e = os.path.join(str(dirpath), str(f))
            file_list.append(e)

for f in file_list:
    print f
    txtfile = open(f, 'r')
    output[f] = []
    for line in txtfile:
        if '<Routine' in line:
            output[f].append(line)

tabs = []
for tab in output:
    tabs.append(tab)

tabs.sort()
for tab in tabs:
    output_file.write(tab + '\n')
    output_file.write('\n')
    for row in output[tab]:
        output_file.write(row + '')
    output_file.write('\n')
    output_file.write('----------------------------------------------------------\n')

raw_input()