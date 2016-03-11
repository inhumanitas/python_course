# coding: utf-8

"""
Создать объект(тип данных) по примеру как namedtuple со следующими свойствами:
- объект инициализируется следующими аргументами:
    1 - выводимое имя типа данных
    *args, **kwargs - определяют внутренний кортеж данных, который доступен
        через обращение как к отрибуту так и получение значения по ключу
        (p.x и p['x'])
- обращение к атрибутам по индексу - p[0]
- добавление любых новых атрибутов после инициализации запрещается -
    p.new_attr = 2  # AttributeError
- присваивание атрибута вызывает исключение типа AttributeError
    p.x = 2
- метод _asdict - возвращает внутренне представление кортежа в виде словаря(dict)
"""
import collections


custom_namedtuple = collections.namedtuple # Change type here

Point = custom_namedtuple('Point', ['x', 'y'])
assert Point.__doc__ == 'Point(x, y)'


x, y = 11, 22
p = Point(x, y=y)
assert p[0] + p[1] == x + y
assert p.x + p.y == x + y

d = p._asdict()

assert {'x': x, 'y': y} == d
