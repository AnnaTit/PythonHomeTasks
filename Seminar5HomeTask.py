# Задача 1
# Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию

def task1():
    from random import randint

    s = int(input("Количество элементов: "))
    lst = [randint(1,11) for _ in range(s)]
    print(f"Сгенерированный список: {lst}")
    print(f"Элементы списка >5: {list(filter(lambda x: x>5, lst))}")


# Задача 2
# Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя

def task2():
    from random import randint

    def sequence(lst):
        last = lst[0]
        for i in range(0, len(lst)):
            if lst[i] >= last:
                last = lst[i]
                if lst[i] not in lst1:
                    lst1.append(lst[i])
        return lst1
        
    n = int(input("Размер исходного списка: "))
    lst = [randint(0, 100) for _ in range(n)]
    lst1 = []
    print(f"Исходный список: \n {lst}")
    print(f"Все возможные возрастающие последовательности списка: ")
    while len(lst) > 1:
        lst1.clear()
        lst1 = sequence(lst)
        lst = lst[1: ]
        if len(lst1) > 1:
            print(lst1)


# Задача 3
# Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.

def task3():
    from random import randint

    n = int(input("Размер исходного списка: "))
    lst = [randint(1,10) for _ in range(n)]

    print(lst)
    lst = list(set(lst))
    print(f"В списке обнаружено {n-len(lst)} повторов.\nСписок без повторов: \n{lst}")

task3()