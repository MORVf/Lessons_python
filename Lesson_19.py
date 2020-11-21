'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран 
в одну строку значения, которые встречаются в нём более одного раза.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
'''

a = [int(i) for i in input().split()] #считываем вводимые числа, приводим к int и формируем список
b = sorted(a)  #сортируем список по возрастанию чисел
j = 0
s = 0

while j < len(b) - 1: #пробегаем все числа списка
    k = j + 1 #будем брать индекс следуещего числа после j
    while k <= len(b) - 1: #пробегаем все числа списка после j
        if b[j] == b[k]:  #если числа равны
            s += 1        #то увеличиваем счетчик
        k += 1            #идём на следующую иттерацию цикла(следующее число списка)
    if s == 1:           #если счетчик==1 <=> это последний индекс, когда будет совпадение конкретного числа с последующим, то
        print(b[j], end=' ') #выводим число данного индекса
    s = 0  #обнуляем счетчик 
    j += 1 #идём на следующую иттерацию цикла(следующее число списка)