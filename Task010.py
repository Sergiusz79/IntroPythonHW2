''' 
Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом 
(положение монет определяет пользователь). 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''

def enter_num_coins():
    try:
        n = int(input("Enter number: \n"))
    except:
        print("Error! This is not integer number!")
    return n

def enter_coin_pos(n):
    count = 0
    obv = 0
    print('Enter coin position 0 - obverse, 1 - reverse: ')
    while count < n:
        pos = int(input())
        if pos == 0:
            obv += 1
        count += 1
    return obv


def counting_num(obv, n):
    rev = n - obv
    if obv < rev:
        print(f'Minimum number of coins to flip is {obv}')
    else:
        print(f'Minimum number of coins to flip is {rev}')

def task():
    n = enter_num_coins()
    obv = enter_coin_pos(n)
    counting_num(obv, n)

task()

'''
Пример идеального решения

n = int(input())
count_zero = 0
count_one = 0
for i in range(n):
x = int(input())
if x == 0:
count_zero += 1
else:
count_one += 1
if count_one > count_zero:
print(count_zero)
else:
print(count_one)
'''