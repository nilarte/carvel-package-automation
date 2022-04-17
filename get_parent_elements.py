import re
import json
def ReadFile(FileName, LineNo):
    ListOfSpace = []
    ListOfStr = []
    ParentElem = []
    Result = []

    for i in range(LineNo - 1, 0, -1):
        with open(FileName) as file:
            ListOfSpace.append(len(re.findall("^ *", file.readlines()[i])[0]))
    for i in range(LineNo - 1, 0, -1):
        with open(FileName) as file:
            ListOfStr.append(file.readlines()[i])
    SpaceCount = int(ListOfSpace[0]) - 2
    file = open(FileName)
    content = file.readlines()
    for i in range(len(ListOfSpace)):
        if ListOfSpace[i] == SpaceCount:
            Result.append(ListOfStr[i])
            SpaceCount = int(ListOfSpace[i]) - 2
            if SpaceCount < 0:
                break
    for i in Result:
        # if it's an array element then get the whole line or parent search will always look for first array element
        if "- " in i.split(':')[0] in i and " {{ include " not in i:
            item = i.strip('\n')
        else:
            item = i.split(':')[0].strip()
        ParentElem.append(item)


    return ParentElem

#parents = ReadFile('D://Nil//charts//bitnami//drupal//templates//deployment.yaml',92)
#print(parents)






