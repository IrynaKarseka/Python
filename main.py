# # Задача 10: 
# # На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# # Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# # повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

# n = int(input('Введите количество монет '))

# gerb = 1
# reshka = 0
# countGerb = 0
# countReshka = 0

# i = 0
# while i < n:
#     enteredNumber = int(input('Введите число:   1 - если "герб",   0 - если "решка"  '))
#     if enteredNumber == reshka:
#         countReshka +=1
#         i += 1
#     elif enteredNumber == gerb:
#         countGerb += 1
#         i += 1
#     else:
#         print('   Можно ввести только "герб" или "решку"')

# if countGerb < countReshka:
#     print(f'Из {n} монет {countGerb} - с "гербами", быстрее перевернуть монеты с "гербом"')
# elif countGerb > countReshka:
#     print(f'Из {n} монет: {countReshka} - с "решками", быстрее перевернуть монеты с "решками"')
# else:
#     print(f'Из {n} монет: {countReshka} - с "решками", {countGerb} - с "гербами", нет разницы, какие монеты переворачивать')
    

# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# while True:
#     x = int(input('Введите первое число (х) задуманное Петей  '))
#     if x > 0 and x <= 1000: 
#         break
#     else:
#         print(f'{x} - число не подходит, оно должно быть от 1 до 1000')

# while True:
#     y = int(input('Введите второе число (у) задуманное Петей  '))
#     if y > 0 and y <= 1000:
#         break
#     else:
#         print(f'{y} - число не подходит, оно должно быть от 1 до 1000') 

# S = x + y
# print(f'Сумма чисел задуманных Петей = {S} - Первая подсказка.')
# P = x * y
# print(f'Произведение чисел задуманных Петей = {P} - Вторая подсказка.')

# for i in range(S):
#     for j in range(S):
#         if i + j == S and i * j == P:
#             print(f'{S} {P} -> {i} {j}')


# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# N = int(input('Введите число N '))
# a = 1

# while a <= N:
#     if a == 1 and N != 1:
#         print(a, end = ' ')
#         a = a * 2
#     else:
#         print(a, end = ' ')
#         a = a * 2
    
