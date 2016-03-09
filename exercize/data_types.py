# coding: utf-8

"""
    Задачи для само проверки
"""

#  1

"""
    Сформировать возрастающий список из четных чисел от 1 до 10 включительно.
"""

int_list = []
i = 1
while i < 11:
    int_list.append(i)
    i += 1

# test
assert int_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#  2

"""
   Сформировать убывающий список из чисел от 10 до 3.
"""

int_list = []
i = 10
while i > 2:
    int_list.append(i)
    i -= 1
# test
assert int_list == [10, 9, 8, 7, 6, 5, 4, 3]

#  3

"""
   Создать список только с четными элементами от 10 до 2.
   Попробовать comprehension и цикл
"""

int_list = []
i = 10
while i > 1:
    if i % 2 == 0:
        int_list.append(i)
    i -= 1
# test
assert int_list == [10, 8, 6, 4, 2]

#  4

"""
    Сформировать матрицу n x m, состоящую из нулей
    Попробовать comprehension и цикл
"""
int_list = []
n = 10
m = 20
for i in range(n):
    int_list.append([])
    for j in range(m):
        int_list[i].append(0)


#  5

"""
    Дан список, вывести максимальный элемент в списке.
"""
int_list = [1, 2, 3, 4, 5, 6, -1, -2, -3]
max_element = None

if int_list.__len__() > 0:
    max_element = int_list[0]

for i in int_list:
    if max_element < int_list[i]:
        max_element = int_list[i]


#  6
"""
    Найти сумму 2/3 + 3/4 + 4/5 +...+ 9/10
"""

i = 2.0
j = 3.0
element_sum = 0.0
for k in range(8):
    element_sum += (i+k)/(j+k)

#  7

"""
    Для произвольной строки получить строку с уникальными символами
    на основе исходной
"""
str_element = 'asw123dasd1234441asdwqqs dadwedq12312weqe45512w'
str1 = ''
for i in str_element:
    if i not in str1:
        str1 += i

#  8

"""
    Для произвольной строки найти кол-во вхождений каждого символа
    Попробовать dict
"""
dict_str = {}
for i in str_element:
    if i not in dict_str:
        dict_str[i] = 1
    else:
        dict_str[i] += 1
#  9
"""
    Удалить в строке все цифры.
"""
for i in range(9):
    str_element = str_element.replace(str(i), '')

#  10

"""
    Описать класс, реализующий десятичный счетчик, который может увеличивать
    или уменьшать свое значение на единицу в заданном диапазоне.
    Предусмотреть инициализацию счетчика значениями по умолчанию и
    произвольными значениями.
    Счетчик имеет 3 метода: увеличения, уменьшения и
    возвращающий текущее состояние счетчика.
    Написать программу, демонстрирующую все возможности класса.

"""