'''
Задача 14: 
Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N.
'''

def enter_num():
    try:
        a = int(input(f"Enter number: \n"))
    except:
        print("Error! This is not integer number!")
    return a


def task():
    n = enter_num()
    pow = 0
    res = 0
    while res <= n:
        res = 2 ** pow
        pow += 1
        if res > n:
            res = 2 ** (pow - 1)
            break
        print(res, end = ' ')

task()


'''
Пример идеального решения

n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1
'''