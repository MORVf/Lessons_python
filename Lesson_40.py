'''
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
На вход программе первой строкой передаётся количество d известных нам слов, после чего на d строках 
указываются эти слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the
'''

count_words_in_set = int(input())   #количество корректных слов для заполнения множества

words = set()   #множество с корректными словами
words_with_fails = set()   #множество со словами, в которых есть опечатки

for i in range(count_words_in_set):  #считываем вводимые слова
    words.add(input().lower())   #добавляем их в множество в нижнем регистре

count_strings_in_text = int(input())  #количество строк в тексте

for j in range(count_strings_in_text):   #считываем вводимые строки
    new_text = input().split()
    for word in new_text:    #проверяем каждое слово в строке
        if word.lower() not in words:   #если его нет в множестве с корректными словами
            words_with_fails.add(word.lower())  #добавляем слово с опечаткой в множество с ошибками

for word_fail in words_with_fails:   #пробегаем множество с опечатками
    print(word_fail) #и выводим каждое слово из него
