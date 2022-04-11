#Find path leading to certain value in helm chart
import yaml

f = open("D://Nil//VMWare_Bitnami_Carvel//Nil//config.yml")
file_content = f.read()
config_files_list = file_content.split('---')

for config_file in config_files_list:
    first_line = config_file.split('\n', 2)[1]
    if '#! Source:' in first_line:
        print(first_line)
        file_name = first_line.rsplit('/', 1)[1]
        print(file_name)
        # open new yaml file
        yaml_file = open("D://Nil//VMWare_Bitnami_Carvel//Nil//output//" + file_name, "w")
        # Always write these 2 lines
        yaml_file.write('#@ load("@ytt:data", "data")\n')
        yaml_file.write('---')
        # write string to file
        yaml_file.write(config_file)
        # close file
        yaml_file.close()
#print(config_files_list)

#yaml_in_dict_fotmat = yaml.load(f, Loader=yaml.FullLoader)
#print(yaml_in_dict_fotmat)
f.close()
