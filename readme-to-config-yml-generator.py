import os
import re
from get_parent_elements import ReadFile

f = open("D://Nil//charts//bitnami//drupal//README.md")
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
            for dirpath, dirnames, files in os.walk('D://Nil//charts//bitnami//drupal//templates'):
                for file_name in files:
                    infile = open('D://Nil//charts//bitnami//drupal//templates//' + file_name, 'r')
                    for num, line in enumerate(infile, 1):
                        if ".Values." + name + " " in line:
                            if ': {{' in line and ' include ' not in line:
                                print(file_name)
                                print(line)
                                print("Found at line: ", num)
                                parents = ReadFile('D://Nil//charts//bitnami//drupal//templates//' + file_name, num)
                                print(parents)
                                print("---------------")
                    #grep_result_list = grep(infile, ".Values." + name + " ")
                    #for single_grep_result in grep_result_list:
                    #    if ': {{' in single_grep_result and ' include ' not in single_grep_result:
                    #        print(file_name)
                    #        print(single_grep_result)
                    #        #print("---------------")
f.close()

#Find path leading to certain value in helm chart
f = open("D://Nil//charts//bitnami//drupal//templates//ingress.yaml")
#yaml_in_dict_fotmat = yaml.load(f, Loader=yaml.FullLoader)
#print(yaml_in_dict_fotmat)
f.close()


