# coding: utf-8

print u"""
Дзэн Питона (Тим Петерс)

Красивое лучше уродливого.
Явное лучше неявного.
Простое лучше сложного.
Сложное лучше запутанного.
Развернутое лучше вложенного.
Разреженное лучше плотного.
Читаемость имеет значение.
Особые случаи не настолько особые, чтобы нарушать правила.
При этом практичность важнее безупречности.
Ошибки не должны замалчиваться.
Если не замалчиваются явно.
Встретив двусмысленность, отбрось искушение угадать.
Должен существовать один - и, желательно, только один - очевидный способ сделать это.
Хотя он поначалу может быть и не очевиден, если вы не голландец.
Сейчас лучше, чем никогда.
Хотя никогда зачастую лучше, чем *прямо* сейчас.
Если реализацию сложно объяснить - идея плоха.
Если реализацию легко объяснить - идея, возможно, хороша.
Пространства имен - отличная штука! Будем делать их побольше!
"""


class AbcDef:
    pass


a = 1


def fn_sum(integer=1):
    """ Function do sum
    :arg integer: first arg
    :return: summ integer + 1
    """
    my_list = [1, 2, 3]
    a = 0
    my_list.append(a)
    return integer + 1


# list comprehension
a = xrange(1, 10)
b = [i for i in a]


# set comprehension
b = {i for i in a}
# print b


# dict comprehension
d_values = {1: '1', 2: '2'}
d = {i: d_values[i] for i in range(10)
     if i in d_values}


# additions
# str
'a' in 'abcde'  # True


# set
1 in {1, 2}  # True


# dict
1 in {1: 1}  # True


1 in [1, 1, 2]  # True


dct = {1: '1', 2: '3', 3: '4'}
d_reverted = {dct[key]: key for key in dct}

for key in d_reverted:
    if False:
        value = d_reverted[key]

# accessing dict items
# d_new[3333]  # KeyError
a = dct.get(3333)  # None
a = dct.get(3333, 'default')  # default


# variables unpacking
list_a = [[1, 2, 3], [2, 2, 2], 'bcq']

for item1, item2, item3 in list_a:
    print item1, item2, item3

a = 1
b = 2
a, b = b, a


# list of all magic variables in globals
globals_d = globals().copy()
print [var for var in globals_d if '__' in var]
