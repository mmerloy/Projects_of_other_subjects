dict = {}
result = []

with open("H://PYTHON/laba/test5_1.txt", "r", encoding="UTF-8") as file1:
    data = file1.read().lower()

    dataSize = len(data)
    for i in range(dataSize):
        key = data[i]
        if not key.isalpha() or key.isascii():
            continue

        if key not in dict.keys():
            dict[key] = '1'
        else:
            dict[key] = str(int(dict[key]) + 1)

    file1.close()

result = list(dict.items())
result.sort(key=lambda i: int(i[1]), reverse=True)

with open("H://PYTHON/laba/test5_2.txt", "w", encoding="UTF-8") as file2:
    for i in result:
        file2.write(i[0] + " : " + i[1] + "\n")
    file2.close()