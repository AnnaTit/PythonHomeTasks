# Задача 1
# Дано натуральное число N. Найдите значение выражения N + NN + NNN
# N может быть любой длины

def task1():
    n = input("Введите целое положительное число: ")
    lst = [n for _ in range(3)]
    lst1 = [int("".join(lst[i: ])) for i in range(3) ]
    lst1.reverse()
    print(f"{''.join(str(lst1))} => {sum(lst1)}")


# Задача 2
# Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёзхначное натуральное число. 
# Напишите программу, которая определяет, есть ли в массиве последовательность из 3х элементов, совпадающая с введённым числом

def task2():
    from random import randint
    arr = []

    def generator():
        return[randint(0,9) for _ in range(15)]

    def sequenceSearch(number):
        string =''
        for c in arr:
            string += str(c)
        if string.__contains__(number):
            print(number)
        else:
            print(f"Не найдено")

    arr = generator()
    print(arr)
    sequenceSearch(input("Введите 3х значное число: "))


# Задача 3
# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def task3():
    def isCommonDivisor(num, denum):
        for i in range(2,12):
            if num %i == 0 and denum %i ==0:
                return True 
        return False 

    for i in range (1,12):
        for j in range (i+1,12):
            if not isCommonDivisor(i,j):
                print(f"{i}/{j}")

task3()
