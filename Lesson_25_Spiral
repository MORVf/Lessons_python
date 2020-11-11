'''
Выведите таблицу размером n x n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла 
и закрученной по часовой стрелке, как показано в примере (здесь n = 5):

Sample Input:
5

Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''

size_field = int(input()) #вводим размер таблицы

field = [[0 for i in range(size_field)] for j in range(size_field)] #инициализируем матрицу и заполняем 0-ми

number = 1 #начальная цифра, которой будет заполняться матрица
save_size_field = size_field #сохраняем размер матрицы в другой переменной 
all_steps = 1 #общий счетчик всех проходов, начальная нумерация проходов с 1 (с левого верхнего угла до конца вправо и в самый низ)
left_down_steps = 0 #счетчик количества проходов именно по пути слева-направо-вниз
right_up_steps = 0 #счетчик количества проходов именно по пути справа-налево-вверх
for size_field in range(size_field, 0, -1):#бежим внутрь матрицы от краёв до центра
    if all_steps % 2 != 0: #если это проход по пути слева-направо-вниз
        j = 0 + left_down_steps #выставляем j согласно счетчику проходов и размера матрицы
        for i in range(0 + left_down_steps, size_field + left_down_steps): #двигаемся слева направо
            while j < size_field + left_down_steps:
                while number <= save_size_field * save_size_field:
                    field[i][j] = number #пишем в клетку цифру
                    number += 1 #увеличиваем цифру
                    break
                if j == size_field + left_down_steps - 1: #если мы достигли края по вертикали, то мы сохраняем j, чтобы двигаться по нему вниз
                    break
                else:
                    j += 1 #идём дальше вправо
        left_down_steps += 1 #увеличиваем количество проходов      
    else: #иначе это проход по пути справа-налево-вверх
        j = size_field + right_up_steps - 1 #выставляем j согласно счетчику проходов и размера матрицы
        for i in range(size_field + right_up_steps, 0 + right_up_steps, -1): #двигаемся справа налево
            while j > right_up_steps - 1:
                while number <= save_size_field * save_size_field:
                    field[i][j] = number #пишем в клетку цифру
                    number += 1 #увеличиваем цифру
                    break
                if j == right_up_steps: #если мы достигли края по вертикали, то мы сохраняем j, чтобы двигаться по нему вверх
                    break
                else:
                    j -= 1 #идём дальше влево
        right_up_steps += 1 #увеличиваем количество проходов   
    all_steps += 1 #cчитываем проходы

#выводим список в виде таблицы
for g in range(save_size_field):
    for v in range(save_size_field):
        print(field[g][v], end=' ')
    print('')
