# 2  вариант
# 1 numb
sum1=0
sum2=0
num = int(input("Введите ,пожалуйста, число "))
while num != 0:
    if num > 0:
        sum1 = sum1 + num
    else:
     sum2 = sum2 + num
    num = 0
    num = int(input("Введите ,пожалуйста, число "))
print("Работа программы завешена")
print("Сумма положительных равна ", sum1)
print("Сумма отрицательных чисел равна ",sum2)