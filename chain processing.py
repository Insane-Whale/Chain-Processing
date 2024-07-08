import math
chaine =  []

iteration = int(input('Itérations: '))

print('\nStart\n')
for iterations in range(iteration):
    num1 = int(input('Number 1: '))
    num2 = int(input('Number 2: '))
    result = (math.sqrt(num1**2)+(num2**2))
    chaine.append(result)

print('\nEnd\n')

for row in chaine:
    print(row)
    print()