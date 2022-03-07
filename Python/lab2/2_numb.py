
minn = ''
maxx = ''
max_index = 0
min_index = 0

with open("text2_1.txt", "r") as fa:
    value = fa.readlines()
    sep_value = value[0].split(";")
    cost = int(sep_value[2])
    max_elem = cost
    min_elem = cost

with open("text2_1.txt", "r") as fa:
    value = fa.readlines()

    value_size = len(value)
    for i in range(0 ,value_size):
        sep_value = value[i].split(";")
        cost = int(sep_value[2])

        if cost >= max_elem:
            max_elem = cost
            max_index = i

        if cost <= min_elem:
            min_elem = cost
            min_index = i

        maxx = value[max_index]
        minn = value[min_index]

        with open("text2_2.txt", 'w') as fs:
            fs.write(minn)
            fs.write(maxx)