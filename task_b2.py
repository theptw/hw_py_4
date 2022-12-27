# B. Даны два файла, в каждом из которых находится запись 
# многочлена. Задача - сформировать файл, содержащий сумму многочленов.
dict1 = {}
dict2 = {}

path = 'mnogochl_1.txt'
data = open(path, 'r')
for line in data:
    var1 = line
data.close()

path = 'mnogochl_2.txt'
data = open(path, 'r')
for line in data:
    var2 = line
data.close()

var1 = var1.replace('*', '') # формирование списков из многочленов для удобной передачи в словарь
var1 = var1.replace('+', '')
var1 = var1.replace('=', '')
var2 = var2.replace('*', '')
var2 = var2.replace('+', '')
var2 = var2.replace('=', '')
var1 = var1.split()
var2 = var2.split()
del var1[-1]
del var2[-1]

print(f'Список из первого файла = {var1}')
print(f'Список из второго файла = {var2}')

def form_dict(list1, list2):
    for b in range(len(list1)):
        x = 3
        koef = ''
        power = ''
        for i in range(len(list1[b])): #перебор вариантов полученных значений и внесение в словарь
            if len(list1[b]) == 1: # Только X
                koef = '1'
                power = '1'
            if len(list1[b]) == 2 and list1[b][1] == 'x': # Число и X после
                koef = list1[b][0]
                power = '1'
            elif len(list1[b]) == 2 and list1[b][0] == 'x': # Х и число после
                power = list1[b][1]
                koef = '1'
            if list1[b][i] == 'x':
                x = i
                if list1[b][-1] == 'x':
                    power = '1'
            if list1[b][i] != 'x' and i < x: # Остальные случаи: если i меньше x добавляем цифру в коэфицент
                koef += list1[b][i]
            elif list1[b][i] != 'x' and i > x and len(list1[b]) > 2: # если больше - в степень
                power += list1[b][i]
        dict1[power] = koef

    for b in range(len(list2)):
        x = 3
        koef = ''
        power = ''
        for i in range(len(list2[b])):
            if len(list2[b]) == 1:
                koef = '1'
                power = '1'
            if len(list2[b]) == 2 and list2[b][1] == 'x':
                koef = list2[b][0]
                power = '1'
            elif len(list2[b]) == 2 and list2[b][0] == 'x':
                power = list2[b][1]
                koef = '1'
            if list2[b][i] == 'x':
                x = i
                if list2[b][-1] == 'x':
                    power = '1'
            if list2[b][i] != 'x' and i < x:
                koef += list2[b][i]
            elif list2[b][i] != 'x' and i > x and len(list2[b]) > 2:
                power += list2[b][i]
        dict2[power] = koef
    return dict1, dict2
        
print(form_dict(var1,var2))

def final_str_original_only(dict1,dict2):
    key_difference1 = dict1.keys() - dict2.keys()
    key_difference2 = dict2.keys() - dict1.keys()
    if len(key_difference1) == 0:
        uni_keys = []
        for key in key_difference2:
            uni_keys.append(key)
    
        uni_values = []
        for i in range(len(uni_keys)):
            uni_values.append(dict2[uni_keys[i]])

        uni_final = []
        for i in range(len(uni_values)):
            uni_final.append(uni_values[i] + '*x**' + uni_keys[i])
        return uni_final
    elif len(key_difference2) == 0:
        uni_keys = []
        for key in key_difference1:
            uni_keys.append(key)
               
        uni_values = []
        for i in range(len(uni_keys)):
            uni_values.append(dict1[uni_keys[i]])

        uni_final = []
        temp = 0
        print(uni_keys)
        print(uni_values)
        for i in range(len(uni_keys)): # перевод в int для сортировки
            uni_keys[i] = int(uni_keys[i])
            uni_values[i] = int(uni_values[i])
        
        for run in range(len(uni_keys) - 1): # сортировка
            for i in range(len(uni_keys) - 1):
                if uni_keys[i] < uni_keys[i+1]:
                    uni_keys[i], uni_keys[i+1] = uni_keys[i+1], uni_keys[i]
                    uni_values[i], uni_values[i+1] = uni_values[i+1], uni_values[i]

        for i in range(len(uni_values)): # формирование финального массива строк уникальных степеней(которые есть только в одном списке)
            uni_final.append(str(uni_values[i]) + '*x**' + str(uni_keys[i]))
        return uni_final

final = final_str_original_only(dict1, dict2)
print(final)


if len(dict2) > len(dict1):
    difference = len(dict2) - len(dict1)
    for i in range(len(dict2), len(dict1), -1):
        dict2.pop(f'{i}')
elif len(dict2) < len(dict1):
    difference = len(dict1) - len(dict2)
    for i in range(len(dict1), len(dict2), -1):
        dict1.pop(f'{i}')
for i in range(len(dict1)):
    final.append(str(int(dict1[f'{len(dict1) - i}']) + int(dict2[f'{len(dict1) - i}'])) + '*x**' + f'{len(dict1) - i}')
        
print(final)
# maxx = 0
# temp = 0
# for i in range(len(final)):
#     for b in range(len(final[i])):
#         if final[i][b] == 'x':
#             x = b
#         if len(final[i][x:]) == 4 and int(final[i][-2:]) > maxx:
#             maxx = final[i]



data = open('sum.txt', 'w')
for i in range(len(final)):
    if i != len(final) - 1:
        data.write(final[i] + ' + ')
    else: data.write(final[i] + ' = 0')
data.close()