import fileinput
import glob

file_list = glob.glob("*.L5X")

with open('NewRoutine.txt', 'w') as file:
    input_lines = fileinput.input(file_list)
    file.writelines(input_lines)