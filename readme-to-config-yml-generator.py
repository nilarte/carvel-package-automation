import os
import re
import json
import argparse
from get_parent_elements import ReadFile
from set_value_via_parent_elements import setValue

#Parse arguments

ap = argparse.ArgumentParser()
ap.add_argument("-cl", "--chartLocation", required=True,
	help="path for specific bitnami application chart folder")
args = vars(ap.parse_args())
chart_location = args["chartLocation"]
print(chart_location)
unsucessfull_additions_list = []
count = 0
f = open(chart_location + '//README.md')
values = f.readlines()
flag = False
values_dict = {}
temp_val = ''
name_dict = current_dict = {}
new = {}
dup_temp_val = ''
for i in values:
    if i.strip(' ') == '\n': continue
    if i.strip(' #\n') == 'Parameters':
        flag = True
    if flag:
        # val = re.search("`(.*)`", i.strip())
        if i.strip(' #\n').endswith('parameters'):
            temp_val = i.strip(' #\n')
            values_dict[temp_val] = []
            continue
        splited_values = list(map(lambda y: y.strip(), i.strip(' |\n').split('|')))
        if splited_values == ['Name', 'Description', 'Value']:
            if len(name_dict) > 0:
                values_dict[dup_temp_val].append(name_dict)
            dup_temp_val = temp_val
            name_dict = current_dict = {}
            new = {}
            continue
        if len(splited_values) == 3 and re.search("`(.*)`", splited_values[0]) and re.search("`(.*)`", splited_values[2]):
            name = re.search("`(.*)`", splited_values[0]).group(1)
            #print(name)
            #print(splited_values[2])
            # Walking a directory tree and printing the names of the directories and files
            for dirpath, dirnames, files in os.walk(chart_location + '//templates'):
                for file_name in files:
                    if file_name.lower().endswith(('.yaml', '.yml')):
                        #infile = open(chart_location + '//templates//' + file_name, 'r')
                        infile = open(dirpath + '//' + file_name, 'r')
                        for num, line in enumerate(infile, 1):
                            if ".Values." + name + " " in line:
                                if ': {{' in line and ' include ' not in line:
                                    count = count + 1
                                    print(name)
                                    print(file_name)
                                    print(line)
                                    split_str_with_colon_and_space = line.split(":")
                                    key_name = ((split_str_with_colon_and_space)[0]).strip()
                                    print(key_name)
                                    print("Found at line: ", num)
                                    #parents = ReadFile(chart_location + '//templates//' + file_name, num)
                                    parents = ReadFile(dirpath + '//' + file_name, num)
                                    # reverse the list to be in right order which is from top to bottom
                                    parents.reverse()
                                    print(parents)
                                    result = ""
                                    try:
                                        result = setValue(file_name, parents, key_name, name)
                                    except:
                                        unsuccessful_entry = {'reason': 'exception', 'name': name, 'file_name': file_name, 'line': line, 'linenum': num}
                                        unsucessfull_additions_list.append(unsuccessful_entry)
                                    if len(result) > 0:
                                        unsuccessful_entry = {'reason': result, 'name': name, 'file_name': file_name, 'line': line, 'linenum': num}
                                        unsucessfull_additions_list.append(unsuccessful_entry)
                                    print("---------------")
f.close()
print("COUNT:" + str(count))
print("following entries could not be added")
for entry in unsucessfull_additions_list:
    print(entry)



