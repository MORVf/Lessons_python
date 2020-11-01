'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, 
потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.
'''

a = int(input())
b = int(input())
c = int(input())
m_max = a
m_min = a
m_other = a
if b > a: 
    if c > a:
        if b > c:
            m_max = b
            m_other = c
            print(m_max)
            print(m_min)
            print(m_other)
        else: # b < c
            m_max = c
            m_other = b
            print(m_max)
            print(m_min)
            print(m_other)
    else: #b > a > c
        m_min = c
        m_max = b
        print(m_max)
        print(m_min)
        print(m_other)
else: # b < a
    if c < a:
        if b < c:
            m_min = b
            m_other = c
            print(m_max)
            print(m_min)
            print(m_other)
        else: # b > c
            m_min = c
            m_other = b
            print(m_max)
            print(m_min)
            print(m_other)
    else: #c > a > b
        m_max = c
        m_min = b
        print(m_max)
        print(m_min)
        print(m_other)
