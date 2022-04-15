import yaml
def setValue(file_name, parent_list, key_name):
    f = open(file_name)
    file_content = f.read()
    content_without_load_statements = file_content.split('---')[1]
    root_parent = yaml.load(content_without_load_statements, Loader=yaml.Loader)
    for index,parent in enumerate(parent_list, 1):
        if not parent.startswith('- '):
            root_parent = root_parent[parent]
        else:
            # Now we are dealing with the list
            for yaml_list_element in root_parent:
                print(index)
                print(parent)
                if index < len(parent_list):
                    # check if next element is there if not backtrack via for loop
                    if parent_list[index + 1] in yaml_list_element:
                        root_parent = yaml_list_element
                        break
                else:
                    # check if final key is there if not backtrack via for loop
                    if key_name in yaml_list_element:
                        root_parent = yaml_list_element
                        break


    print(root_parent)
    print(root_parent[key_name])

# parent_list = ['- name', 'containers', 'spec', 'template', 'spec']
# parent_list.reverse()
# setValue("D://Nil//VMWare_Bitnami_Carvel//Nil//output//deployment.yaml", parent_list, "imagePullPolicy")