dict = {}
result = []

with open("H://PYTHON/laba/intest4_1.txt", "r") as infile1:
    data = infile1.read()

    words = data.split(',')
    wordsSize = len(words)
    for i in range(wordsSize):
        key = words[i]

        dict[key] = '1'

with open("H://PYTHON/laba/intest4_2.txt", "r") as infile2:
    data = infile2.read()

    words = data.split(',')
    wordsSize = len(words)
    for i in range(wordsSize):
        key = words[i]

        if key not in dict.keys():
            result.append(key)

with open("H://PYTHON/laba/outtest4_1.txt", "w") as outfile1:
    outputSize = len(result)

    for i in range(outputSize):
        outfile1.write(result[i] + "\n")

