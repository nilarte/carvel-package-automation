import re
import copy
f=open("D://Nil//charts//bitnami//drupal//README.md")
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
            # name_dict = current_dict = {}
            name_dict = current_dict = new
            for name1 in name.split('.'):
                if name1 not in current_dict:
                    current_dict[name1] = {}
                # else:
                #     current_dict = name_dict
                if name1 == name.split('.')[-1]:
                    current_dict[name1] = {'description': splited_values[1], 'value' : re.search("`(.*)`", splited_values[2]).group(1)}
                else:
                    current_dict = current_dict[name1]

            new = copy.deepcopy(name_dict)

            current_dict[name.split('.')[-1]] = {'description': splited_values[1], 'value' : re.search("`(.*)`", splited_values[2]).group(1)}



if len(name_dict) > 0:
    values_dict[dup_temp_val].append(name_dict)

# print(values_dict)

f.close()

f1= open('test.yml', 'w')

y=''

for key, value in values_dict.items():
    y +='\n\n#!' + key +':'
    for key1, val1 in value[0].items():
        if 'description' in val1:
            y += '\n#@schema/desc ' + val1['description']
            y += '\n'+key1 + ': ' + val1['value']
        else:
            y += '\n'+key1 + ':'
            for key2, val2 in val1.items():
                if 'description' in val2:
                    y += '\n  #@schema/desc ' + val2['description']
                    y += '\n  ' + key2 + ': ' + val2['value']
                else:
                    y += '\n  ' + key2 + ':'
                    for key3, val3 in val2.items():
                        if 'description' in val3:
                            y += '\n    #@schema/desc ' + val3['description']
                            y += '\n    ' + key3 + ': ' + val3['value']

f1.write(y)
f1.close()
