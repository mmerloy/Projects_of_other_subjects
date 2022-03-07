# 2  вариант
# 2 numb

num = int(input("Введите пожалуйста число N для вывода всех автоморфных чисел , не превышающих его "))
for i in range(1, num + 1):
    f = str(i)
    dlina1 = len(f)
    f2 = str(i ** 2)
    dlina2 = len(f2)
    if f2[dlina2 - dlina1:dlina2] == f:
        print(i)

print("Работа программы завешена")
