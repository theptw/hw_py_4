# A. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0
#  или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень многочлена: '))

powers = [x for x in range(1,k+1)] # Создание списка степеней переменных
print(powers)

my_dict = dict.fromkeys(powers)  # Добавление степеней в словарь(ключи)

for i in range(k):
    my_dict[list(my_dict.keys())[i]] = random.randint(0,100) # Добавление рандомных коэфицентов в словарь(значения)
print(my_dict)

def final_list(dict): # формирования списка нужного формата из словаря
    count = 0
    solution = []

    for key, value in my_dict.items():
        count += 1
        if count == 1:
            solution.append(str(value) + f'*x')
        elif value == 0:
            solution.append(f'x**{key}')
        else:
            solution.append(str(value) + f'*x**{key}')
    solution.reverse()
    return solution
print(final_list(my_dict))

data = open('mnogochl_2.txt', 'w')
for i in range(k):
    if i < k - 1:
        data.write(final_list(my_dict)[i] + ' + ')
    else:
        data.write(final_list(my_dict)[i] + ' = 0')
data.close()

