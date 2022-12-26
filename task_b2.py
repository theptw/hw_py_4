my_dict = {}

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
print(var1)
var1 = var1.replace('*', '')
print(var1)
var1 = var1.replace('+', '')
var1 = var1.replace('=', '')
var2 = var2.replace('*', '')

print(var1)

var1 = var1.split()
print(var1)
del var1[-1]
print(var1)

koef = ''
power = ''

for b in range(len(var1)):
    x = 3
    koef = ''
    power = ''
    for i in range(len(var1[b])):
        if len(var1[b]) == 1:
            koef = '1'
            power = '1'
        if len(var1[b]) == 2 and var1[b][1] == 'x':
            koef = var1[b][0]
            power = '1'
        elif len(var1[b]) == 2 and var1[b][0] == 'x':
            power = var1[b][1]
            koef = '1'
        if var1[b][i] == 'x':
            x = i
            if var1[b][-1] == 'x':
                power = '1'
        if var1[b][i] != 'x' and i < x:
            koef += var1[b][i]
        elif var1[b][i] != 'x' and i > x and len(var1[b]) > 2:
            power += var1[b][i]
    my_dict[power] = koef
    


ndict = {**my_dict}
print(ndict)

