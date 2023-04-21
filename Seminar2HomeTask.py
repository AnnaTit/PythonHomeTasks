# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.

def task1():
    number = int(input('Введите число: '))
    numbers = []
    value = 1
    for i in range(1, number + 1):
        numbers.append(value)
        value *= i + 1
    print(f'Факториалы для чисел от 1 до {number} следующие: {numbers}')

# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def task2():
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                print(f'{x} | {y} | {z} | {bool((not(x and y) or z))}')
    
# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
def task3():
    string1 = input('Введите первую строку: ')
    string2 = input('Введите вторую строку:')
    count = 0
    print(f'{string1}, {string2} - ', end=' ')   
    for i in string1:
        for j in string2:
            if i == j:
                count +=1
        print(f'{i} - {count}', end=" ")
        count = 0


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def task4():
    n = int(input('Введите число: '))
    lst = [n-1, n]
    for i in range(-n, n-1):
        lst.append(i)
    print(lst)

task4()

