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
        #item = i.split(':')[0].strip()
        #ParentElem.append(item)
        ParentElem.append(i.strip('\n'))

    return ParentElem

parents = ReadFile('D://Nil//charts//bitnami//drupal//templates//deployment.yaml',92)
print(parents)






