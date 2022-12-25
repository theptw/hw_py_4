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
var1 = var1.replace('0', '')
print(var1)


var1 = var1.split()
print(var1)

koef1 = ''
power = ''
x = 3
for b in range(len(var1)):
    help_koef1 = koef1
    
    koef1 = ''
    power = ''
    for i in range(len(var1[b])):
        # if var1[b][i] != 'x' and i < x:
        #     koef1 += var1[b][i]
        if var1[b][i] == 'x' and len(var1[b]) - len(var1[b][i:]) == 1:
            koef1 += var1[b][i-1]
            x = i
        elif var1[b][i] == 'x' and len(var1[b]) - len(var1[b][i:]) == 2:
            koef1 += var1[b][i-2] + var1[b][i-1]
            x = i
        elif var1[b][i] == 'x' and len(var1[b]) - len(var1[b][i:]) == 0:
            koef1 = '1'
            x = i
        elif i > x:
            power += var1[b][i]
        elif var1[b][i] == 'x':
            power = '1'
        # elif i > x and len(var1[b]) - i == 1:
        #     power = var1[b][i]
        # elif i > x and len(var1[b]) - i == 2:
        #     power = var1[b][i] + var1[b][i+1]
        # elif i > x and len(var1[b]) - i == 0:
        #     power = '1'
    my_dict[power] = koef1
        
        
        
        



print(my_dict)

# if var1[b][i] == 'x' and len(var1[b]) - (i+1) == 1:
#             my_dict[var1[b][i+1]] = var1[b][i-1]