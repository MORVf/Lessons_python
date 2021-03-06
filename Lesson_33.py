'''
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, 
и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
'''

import os       #импортируем модуль

file_in = os.path.join('C:\\', 'Documents', 'in.txt')    #формируем путь до входного файла
file_out = os.path.join('C:\\', 'Documents', 'out.txt')  #формируем путь до выходного файла

with open(file_in, 'r') as f_in:   #открываем входной файл на чтение
    s = f_in.readline().strip()    #считываем строку из файла и убираем лишние символы/пробелы слева и справа от текста

n_int = '' #инициализация пустой строки, где мы будем конкатинировать все цифры, идущие друг за другом во входной строке из файла
lst = [] #инициализация пустого списка, куда мы запишем промежуточный результат, состоящий из строк и цифр
result = '' #инициализация итоговой строки, которая будет записываться в выходной файл

for k in range(len(s)): #пробегаем все индексы элементов входного текста из входного файла
    i = 0
    while i < 10: #пробегаем все цифры от 0 до 9
        if s[k] == str(i) and k != len(s) - 1: #если символ в строке является цифрой и он не последний, то
            n_int += s[k]  #накапливаем его в специальной строке
            break          #завершаем цикл и переходим к следующему символу входной строки
        elif s[k] == str(i) and k == len(s) - 1:  #если символ в строке является цифрой и он последний, то
            lst += [int(s[k])]      #сразу записываем число в список
            break   #завершаем цикл
        else: #если символ в строке не является цифрой, то
            if i != 9: #если мы символ входной строки не сравнили со всеми цифрами, то
                i += 1  #идём сравнивать с бОльшим числом
            else:      #если мы символ входной строки сравнили со всеми цифрами, то
                if n_int != '':    #если к этому времени мы успели накопить цифры за счет предыдущих элементов входной строки
                    lst += [int(n_int)] #то записываем накопленные сконкатенированные цифры в виде числа в список 
                    lst += s[k]  #после этого записываем символ из входной строки, идущий после цифр, в список
                    n_int = ''  #обнуляем накопительную строку для следующих цифр из входной строки 
                    break  #завершаем цикл
                else:    #если к этому времени мы НЕ успели накопить цифры за счет предыдущих элементов входной строки
                    lst += s[k]   #то сразу записываем символ из входной строки в список
                    break       #завершаем цикл

for s in range(0, len(lst), 2):      #пробегаем все строки из списка
    for n in range(1, len(lst), 2):  #пробегаем все цифры из списка
        if n == s + 1:    #если цифра идёт сразу после строки, то
            composition = lst[s] * lst[n]  #перемножаем строку и цифру
    result += composition   #записываем результат произведения в итоговую строку, которая потом пойдет в выходной файл

with open(file_out, 'w') as f_out:   #открываем/создаём выходной файл на запись
    f_out.write(result)   #записываем итоговую строку в файл
