'''
Даны размеры поля для игры в "Сапёр" и координаты мин, стоящих на этом поле. Вывести поле игры на экран.
* - мины, . - отсутствие мин рядом и в самой клетке.

Пример ввода:
 5 4 4 - размеры поля и количество мин
 1 1 - координаты 1 мины
 2 2 - координаты 2 мины
 3 2 - координаты 3 мины
 4 4 - координаты 4 мины
Пример вывода:
*21.
3*2.
2*31
112*
..11
'''

a = [int(i) for i in input().split()] #вводим размеры поля и количество мин, и сохраняем список

c = [] #инициализация списка с координатами мин
for j in range(a[2]): #задаём координаты мин
    b = [int(k) for k in input().split()]
    c += [b]

field = [[0 for v in range(a[1])] for g in range(a[0])] #инициализируем пустое минное поле
#заполняем клетки поля минами
for g in range(len(field)): #горизонталь минного поля
    for v in range(len(field[0])): #вертикаль минного поля
        for ci in range(len(c)):#берём координату мины по горизонтали
            for cj in 0, 1: #берём координату мины по вертикали
                if g == c[ci][0] - 1 and v == c[ci][1] - 1: #если координаты мины и поля совпали, то
                    field[g][v] = '*' #проставляем мину

#проставляем счетчики в клетках поля по количеству мин рядом с ними
count_g = 0 #счетчик смены горизонтали
for g in range(len(field)): #горизонталь минного поля
    count_v = 0 #счетчик смены вертикали
    for v in range(len(field[0])): #вертикаль минного поля
        if field[g][v] != '*': #если в клетке поля нет мины, то
            if count_g > 0: #если горизонталь менялась, то
                l = g - 1 #сдвигаем индекс клетки на 1 назад по горизотали
            else:  #если не менялась, то
                l = 0 #обнуляем индекс клетки по горизонтали
            count_mines = 0 #инициализация счётчика мин
            #пробегаем все сопредельные клетки рядом для поиска мин вокруг НЕминной выбранной клетки
            while l < a[0] and l <= g + 1: #по горизонтали
                if count_v > 0: #если вертикаль менялась, то
                    m = v - 1 #сдвигаем индекс клетки на 1 назад по вертикали
                else:  #если не менялась, то
                    m = 0 #обнуляем индекс клетки по вертикали
                while m < a[1] and m <= v + 1: #по вертикали
                    if field[l][m] == '*': #если в клетке найдена мина, то
                        count_mines += 1 #считываем её и увеличиваем сам счетчик
                        field[g][v] = count_mines #записываем значение счетчика в клетку
                    m += 1 #смотрим следующую клетку по вертикали
                l += 1 #смотрим следующую клетку по горизонтали
        count_v += 1 #меняется вертикаль
    count_g += 1 #меняется горизонталь
        
#клетки поля, где нет ни рядом, ни прямо в ней ни одной мины, и остался 0, заменяем на '.'
for g in range(len(field)): #горизонталь минного поля
    for v in range(len(field[0])): #вертикаль минного поля
        if field[g][v] == 0: #если в клетке находится цифра 0, то
            field[g][v] = '.' #меняем её на '.'
        print(field[g][v], end='') #выводим строку минного поля
    print('') #переход на новую строку минного поля
