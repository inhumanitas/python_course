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


class ReadOnlyTuple(object):
    _tuple = None
    base_name = None
    __var_dct = ()
    allow_attrs = True

    def __init__(self, *args, **kwargs):

        self.__var_dct = collections.OrderedDict(zip(self._tuple, args))
        for key in kwargs:
            if key in self.__var_dct:
                raise TypeError(
                    'got multiple values for keyword argument "{0}"'.format(key))
            self.__var_dct[key] = kwargs[key]

        self.__repr = lambda: u'{name}({params})'.format(
            name=self.base_name, params=', '.join(self._tuple))
        self.__doc__ = self.__repr()
        self.allow_attrs = False

    def __str__(self):
        return self.__repr()

    def __getattr__(self, item):
        if item in self.__var_dct:
            return self.__var_dct[item]

        raise AttributeError(str(item)+' not found')

    def __getitem__(self, item):
        return self.__var_dct[self._tuple[item]]

    def __setattr__(self, key, value):
        if (not self.allow_attrs and
                    key not in self.__var_dct and
                    key not in self._tuple):
            raise AttributeError("can't set attribute '%s'" % key)

        return super(ReadOnlyTuple, self).__setattr__(key, value)

    def _asdict(self):
        return dict(self.__var_dct)


def my_named_tuple(name, *args, **kwargs):
    tpl = []
    for arg in args:
        if isinstance(arg, basestring):
            tpl.extend([var for var in arg.split() if var[0].isalpha()])
            break
        else:
            for var in arg:
                if var[0].isalpha():
                    tpl.append(var)
    tpl = tuple(tpl)
    # doc string for new type
    doc = u'{name}({params})'.format(name=name, params=', '.join(tpl))
    # creating type
    obj = type(name, (ReadOnlyTuple, ),
               {'__doc__': doc, 'base_name': name, '_tuple': tpl})
    return obj


# custom_namedtuple = collections.namedtuple  # Change type here
custom_namedtuple = my_named_tuple  # Change type here

Point = custom_namedtuple('Point', ['x', 'y'])
assert Point.__doc__ == 'Point(x, y)'
Point = custom_namedtuple('Point', 'x y')
assert Point.__doc__ == 'Point(x, y)'


x, y = 11, 22
p = Point(x, y=y)
assert p[0] + p[1] == x + y
assert p.x + p.y == x + y

d = p._asdict()

assert {'x': x, 'y': y} == d

# checking getattr
try:
    p.d
except AttributeError:
    pass
else:
    assert False

# add new attr
try:
    p.z = 2
except AttributeError:
    pass
else:
    assert False, 'Assigment should not be passed'

p2 = Point(33)
p2.y = y
assert p2.y == y
assert p[0] != p2[0]
