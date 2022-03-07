def simple_number(x):
    count = 0
    for numbers in range(1, x+1):
        if x % numbers == 0 and x != 1:
          count += 1
    if count == 2:
       return x
    elif count != 2:
       return -1

def cortej(a, b):
    default = []
    for item in range(a, b + 1):
       default.append(item)
    res = list()
    for numbers in default:
       res.append(simple_number(numbers))
    res = list(filter(lambda x: x > -1, res))
    res = tuple(res)
    return res


print("Программа будет находить простые числа на помежутке ")
print("Введите диапазон чисел")
a = int(input("Введите от какого числа : "))
b = int(input("И до какого числа: "))
if a<0 or b<0 :
    print ("Введено отрицательное число.Введите положительные")
else:
 print("Кортеж из положительных чисел: ")
 print(cortej(a, b))


