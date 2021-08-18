from itertools import cycle

my_list = ['Вышел', 'зайчик', 'на', 'крыльцо']
for el in cycle(my_list):
    print(el)
