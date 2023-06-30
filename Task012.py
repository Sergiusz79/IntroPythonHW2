'''
Задача 12: 
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
'''


def enter_num(text):
    try:
        n = int(input(f"Enter {text} numbers: \n"))
    except:
        print("Error! This is not integer number!")
    return n

def two_numbers(prod, sum):
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i * j == prod and i + j == sum:
                print(f'Numbers conceived by Petya is {i} and {j}')
                return
     
                   

def task():
    prod = enter_num("the product of ")
    sum = enter_num("the sum of numbers")
    two_numbers(prod, sum)

task()    
