# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов N:      '))
print(' ')
m = int(input('Введите количество элементов M:       '))
list_n = []
list_m = []
unite_list = []

for i in range(n):
    list_n.append(int(input('введите целое число N:       ')))

for k in range(m):
    list_m.append(int(input('введите целое число M:       ')))
           
for i in list_n:
    if i in list_m and i not in unite_list:
        unite_list.append(i)

unite_list.sort()            
print(unite_list)