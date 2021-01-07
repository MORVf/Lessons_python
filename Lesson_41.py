'''
Группа биологов в институте биоинформатики завела себе черепашку.
После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное расстояние 
в сантиметрах, которое должна пройти черепашка.
Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу, которая определит, 
куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу, которая выведет точку, в которой 
окажется черепашка после всех команд. Для простоты они решили считать, что движение начинается в точке (0, 0), и движение на восток 
увеличивает первую координату, а на север — вторую.
Программе подаётся на вход число команд n, которые нужно выполнить черепашке, после чего n строк с самими командами. Вывести нужно 
два числа в одну строку: первую и вторую координату конечной точки черепашки. Все координаты целочисленные.

Sample Input:
4
север 10
запад 20
юг 30
восток 40

Sample Output:
20 -20
'''

n = int(input()) #считываем количество команд черепахе

dict_directions = {}   #словарь для хранения направлений и расстояний

for i in range(n):  #считываем направления и расстояния
    direction = input().split()
    if direction[0] in dict_directions.keys(): #если в словаре уже есть такое направление
        dict_directions[direction[0]] = dict_directions[direction[0]] + int(direction[1])   #то суммируем расстояния
    else:  #иначе
        dict_directions[direction[0]] = int(direction[1])   #добавляем новое направление и его расстояние

x = 0  #первая координата
y = 0  #вторая координата

for key in dict_directions.keys():  #проходим по всем направлениям и расстояниям
    if key == 'север':
        y += dict_directions[key]
    if key == 'запад':
        x -= dict_directions[key]
    if key == 'юг':
        y -= dict_directions[key]
    if key == 'восток':
        x += dict_directions[key]

print(x, y)  #выводим конечные координаты