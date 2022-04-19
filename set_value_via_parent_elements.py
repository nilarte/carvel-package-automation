import re
import json
def setValue(FileName, parent_list, key_name, value_name):
    automation_output_parent_dir = "D://Nil//VMWare_Bitnami_Carvel//Nil//output"
    with open(automation_output_parent_dir + "//" + FileName) as file:
        start_line_num = 0
        text = file.readlines()
        for parent in parent_list:
            parent_found = False
            for i in range(start_line_num, len(text)):
                if parent in text[i].strip('\n'):
                    start_line_num = i
                    parent_found = True
                    break
            if not parent_found:
                result = "parent not found: " + parent
                return result
        print(start_line_num)
        key_found = False
        for i in range(start_line_num, len(text)):
            if key_name in text[i]:
                key_found = True
                start_line_num = i
                line_with_key = text[i]
                str_old_value = line_with_key.split(":")[1]
                if " #@ data.values." in str_old_value:
                    print("DOUBLE!!!")
                line_with_key = line_with_key.replace(str_old_value, " #@ data.values." + value_name + '\n')
                text[i] = line_with_key
                break
        if not key_found:
            result = "key not found: " + key_name
            return result
        with open(automation_output_parent_dir + "//" + FileName, "w") as output_file:
            output_file.writelines(text)
        print(start_line_num)
        return ""


#parent_list = ['spec:', '  template:', '    spec:', '      containers:', '        - name: metrics']
#parent_list.reverse()
#setValue("D://Nil//VMWare_Bitnami_Carvel//Nil//output//deployment.yaml", parent_list, "         imagePullPolicy:", "dum")





