
def func_intersection(*params):
    result = set(params[0])

    for i in range(1, len(params)):
        result = result.intersection(params[i])

    return result

#Тестовая программа
a = [1, 2, 3, 4, 5, 9]
b = [4, 5, 6, 7, 8, 9]
c = [9, 5]

print(a,b,c)
print("Программа вернет пересечения множеств")
print(func_intersection(a, b, c))