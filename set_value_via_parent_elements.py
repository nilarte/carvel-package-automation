import re
import json
def setValue(FileName, parent_list, key_name, value_name):

    with open(FileName) as file:
        start_line_num = 0
        text = file.readlines()
        for parent in parent_list:
            for i in range(start_line_num, len(text)):
                if parent == text[i].strip('\n'):
                    start_line_num = i
                    break

        print(start_line_num)
        for i in range(start_line_num, len(text)):
            if key_name in text[i]:
                start_line_num = i
                line_with_key = text[i]
                str_old_value = line_with_key.split(":")[1]
                line_with_key = line_with_key.replace(str_old_value, " " + str(start_line_num + 1) + '\n')
                text[i] = line_with_key
                break
        with open("D://Nil//VMWare_Bitnami_Carvel//Nil//automation-output//deployment.yaml", "w") as output_file:
            output_file.writelines(text)
        print(start_line_num)


parent_list = ['spec:', '  template:', '    spec:', '      containers:', '        - name: metrics']
parent_list.reverse()
setValue("D://Nil//VMWare_Bitnami_Carvel//Nil//output//deployment.yaml", parent_list, "         imagePullPolicy:", "dum")





