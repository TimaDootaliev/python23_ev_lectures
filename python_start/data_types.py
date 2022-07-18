""" Типы данных """

# Изменяемые типы данных:
# list - список
# set - множество
# dict - словари

"""
Неизменяемые типы данных:
tuple - кортеж
str - строки(string)
bool - логический тип/булевый тип (True/False)
int - целые числа(integer)
float - дробные числа/числа с плавающей точкой
complex - сложные числа
frozenset - неизменяемое множество
NoneType - тип данных для обозначения пустого значения (None)
"""


"""
Переменные
"""
# a = 1
# b = int(2)

# Название переменной не должно начинаться с цифр или спец символов
# num = 10 # OK
# 1num = 10 # Error - SyntaxError
# %, &, ?, /, $, !
# $num = 20 # Error

# Если название переменной состоит из нескольких слов, стоит разделять их нижним подчеркиванием(underscore). Разделение слов не должно содержать спец символов и пробелов.

# my_num = 33 # OK - snake_case
# myNum = 34 # OK - camelCase - свойственно для JS

# my-num = 30 # Error
# my num = 54 # Error

# Названия переменных не должны совпадать с названиями ключевых(зарезервированных) слов.
# print = 32 # Error
# for = 54 # Error

# Регистр в питоне играет важную роль
# a = 10
# A = 20
# num = 30
# nUm = 30


# Переменные состоящие из символов верхнего регистра(заглавными буквами) по общему соглашению являются константами(неизменяемыми/постояными)

# URL = 'google.com'

# Хорошая практика: называть переменные так, чтобы было понятно, что они в себе хранят
# литералы - символы, служащие для обозначения данных
# num = 10
# my_float = 20.3
# string = "I'm walking"
# list_of_nums = [1, 2, 3]
# tuple_of_nums = (1, 2, 3)
# set_of_nums = {2, 3.4, 5}
# dictionary = {'word': 'слово'}
# nonetype = None
# true = True
# false = False

"""
Многострочные комментарии
Чаще используются для написания документации к коду
"""
# Однострочный комментарий - используется для краткого описания строки
# a = 10 # some comment

# моя_переменная = 10 # Можно, но нежелательно

"""  
Функции print(), input(), type(), id()
"""

# print(12)
# a = 'Hello world!'
# print(a)
# print() - функция для вывода информации в терминал
# input() - функция для ввода информации из терминала

# string = input()
# print(string)

# age = input('Введите возраст: ')
# print('Ваш возраст: ', age)


# age = int(input('Введите возраст: '))
# print('Ваш возраст: ', age)


# Python - язык с динамической типизацией и строгой типизацией
# a = 10
# str(a) # '10'
# float(a) # 10.0

# 'string' + 10 # Error - TypeError


# num = 22
# print(type(num))
# print(type('asdfasdf'))
# type() - функция для вывода типа переданных данных

a = 10324234234
b = 1033324
print(id(a))
print(id(b))