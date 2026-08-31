"""
filme = ['Matrix', 1999, 8.7, True]

print(filme)   

list = [1,4,2,3,5,6,7]

print(list[:2])

print(list[-1])

print(len(list))

print('O número UM está na posíção: ', list.index(1) + 1)

list.append(8)

for i in list:
    print(i)

list.sort()

print('-'*20)

for i in list:
    print(i)

listCopy = list.copy()
listCopy.remove(8)

print('-'*20)

for i in listCopy:
    print(i)

list.clear()
print(list)
"""


list = [int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))]

print(list)

print(list[0])

sum = 0

for i in list:
    sum += i
    
print(sum)