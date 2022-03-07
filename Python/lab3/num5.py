def monotony_of_sequence(arr):

    varType = type(arr)
    if (varType is int or varType is float or varType is str):
        print("ERROR::WRONG_DATA_TYPE")
        return False

    ans = True
    is_greater = True
    is_less=False


    arrSize = len(arr)
    for i in range(1, arrSize):
        if arr[i] == arr[i - 1]:
            continue

        if arr[i] > arr[i - 1]:
            if  not is_less:
                continue

            if not is_greater:
                ans = False
                return ans
        elif arr[i] < arr[i - 1]:
            if not is_less:
                is_less = True
                is_greater = False
                continue

            if  is_greater:
                ans = False
                return ans

    return ans

#Тестовая программа
input1 = [1, 1, 2, 5, 7, 9]
input2=[9,5,3,1]
input3=[13,1,23,4,5,6,7]
print("Последовательность монотонна? " + str(monotony_of_sequence(input1)))
print("Последовательность монотонна? " + str(monotony_of_sequence(input2)))
print("Последовательность монотонна? " + str(monotony_of_sequence(input3)))