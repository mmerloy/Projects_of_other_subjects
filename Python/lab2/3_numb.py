import os


def getListOfFiles(dirName):

    list_of_file = os.listdir(dirName)
    all_files = list()

    for entry in list_of_file:
        full_path = os.path.join(dirName, entry)
        if os.path.isdir(full_path):
             all_files = all_files + getListOfFiles(full_path)
        else:
            all_files.append(full_path)

    return all_files


data = getListOfFiles(os.getcwd())
#print(data)
dataSize = len(data)

result = []
for i in range(dataSize):
    fileSize = os.stat(data[i]).st_size / (1024 * 1024)

    if (fileSize <= 1):
        result.append(data[i])

with open("H://PYTHON/laba/newtext.txt", "w") as file:
    resultSize = len(result)

    for i in range(resultSize):
        file.write(result[i] + "\n")


