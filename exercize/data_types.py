# coding: utf-8

"""
    Задачи для само проверки
"""

#  1

"""
    Сформировать возрастающий список из четных чисел от 2 до 10 включительно.
"""
int_list = []
int_list2 = []
n = 10
for i, val in enumerate(range(n+1)):
    if i // 2:
        int_list.append(val)

int_list = [x for i, x in enumerate(range(2, n+1)) if i % 2 == 0]
# test
assert int_list == [2, 4, 6, 8, 10]

int_list = [x for x in range(2, n+1, 2)]

# test
assert int_list == [2, 4, 6, 8, 10]


#  2

"""
   Сформировать убывающий список из чисел от 10 до 3.
"""

int_list = [x for x in range(n, 2, -1)]
# test
assert int_list == [10, 9, 8, 7, 6, 5, 4, 3]

#  3

"""
   Создать список только с четными элементами от 10 до 2.
   Попробовать comprehension и цикл
"""

int_list = [x for x in range(n, 1, -2)]
# test
assert int_list == [10, 8, 6, 4, 2]


#  4

"""
    Сформировать матрицу n x m, состоящую из нулей
    Попробовать comprehension и цикл
"""
n = 10
m = 5
matrix = []
for x in range(n):
    matrix.append([])
    for y in range(m):
        matrix[x].append(0)


def test_matrix(matrix):
    assert len(matrix) == n
    for x in matrix:
        assert len(x) == m, 'Wrong matrix dimension'

    matrix[0][1] = 1
    assert matrix[0][1] == 1 and matrix[0][0] == 0, \
        'All items are the same object'

test_matrix(matrix)
# comprehension
matrix_c = [[0 for y in range(m)] for x in range(n)]

test_matrix(matrix_c)

#  5

"""
    Дан список, вывести максимальный элемент в списке.
"""

lst = [1, 2, -4, 222, 4, 150]


def get_max(l):
    assert l, 'Empty list is not supported'

    max_el = l[0]
    for el in l:
        if max_el < el:
            max_el = el
    return max_el

assert max(lst) == get_max(lst)

#  6
"""
    Найти сумму 2/3 + 3/4 + 4/5 +...+ 9/10
"""

summ = reduce(lambda x, y: x + y/float(y+1), range(2, 10), 0.0)

assert sum([n/float(n+1) for n in range(2, 10)]) == summ

#  7

"""
    Для произвольной строки получить строку с уникальными символами
    на основе исходной
"""

string = 'AAbbBBca'

# order doesn't matter
assert set('AbBca') == set(string)


def parse_uniques(string):
    res_str = []
    for char in string:
        if char not in res_str:
            res_str.append(char)
    return res_str

assert 'AbBca' == ''.join(parse_uniques(string))
assert 'AbBca' == reduce(lambda res, ch: res if ch in res else res+ch, string)


#  8

"""
    Для произвольной строки найти кол-во вхождений каждого символа
    Попробовать dict
"""

search_string = 'BAAAvvvBBBdaA'
valid_result = {
    'A': 4,
    'B': 4,
    'a': 1,
    'd': 1,
    'v': 3,
}

import collections

char_count = collections.defaultdict(int)
for char in search_string:
    char_count[char] += 1

assert valid_result == char_count


#  9
"""
    Удалить в строке все цифры.
"""

various_string = 'ABC123C3d9zzz'
result1 = ''.join([char for char in various_string if char.isalpha()])
result2 = reduce(lambda x, y: x+y if y.isalpha() else x, various_string)

assert result1 == result2

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


class Integer(object):

    def __init__(self, *args, **kwargs):
        """ Create integer counter from min to max with given step
        :param min: starting point for values, default is 0
        :param max: maximum element for counter, default is endless count
        :param step: step for counter, default is 1
        """
        super(Integer, self).__init__()
        self._min, self._max, self._step = self.parse_args(*args, **kwargs)
        self.__cur = self._min

    def parse_args(self, *args, **kwargs):
        len_args = len(args)
        len_kwargs = len(kwargs)
        if len_args == 0:
            _max = kwargs.pop('max', None)
            _min = kwargs.pop('min', 0)
            _step = kwargs.pop('step', 1)
        elif len_args == 1:
            _max = args[0]
            if 'max' in kwargs:
                raise ValueError('Wrong input arguments')
            _min = kwargs.pop('min', 0)
            _step = kwargs.pop('step', 1)
        elif len_args == 2:
            _min, _max = args
            if 'min' in kwargs or 'max' in kwargs:
                raise ValueError('Wrong input arguments')
            _step = kwargs.pop('step', 1)
        elif len_args == 3 and len_kwargs == 0:
            _min, _max, _step = args
        else:
            raise ValueError('Wrong input arguments')
        return _min, _max, _step

    def __iter__(self):
        return self.next()

    def next(self):
        while self._max is None or self.__cur < self._max:
            yield self.__cur
            self.__cur += self._step

        raise StopIteration()

    def previous(self):
        self.__cur -= self._step
        if self.__cur < self._min:
            raise StopIteration()

        return self.__cur

    def current_value(self):
        return self.__cur


# Arguments test
i = Integer()
assert i._max is None and i._step == 1 and i._min == 0

i = Integer(10)
assert i._max == 10 and i._step == 1 and i._min == 0

i = Integer(1, 10)
assert i._max == 10 and i._step == 1 and i._min == 1

i = Integer(1, 10, 2)
assert i._max == 10 and i._step == 2 and i._min == 1

i = Integer(min=1, max=10, step=2)
assert i._max == 10 and i._step == 2 and i._min == 1

i = Integer(10, min=1, step=2)
assert i._max == 10 and i._step == 2 and i._min == 1

i = Integer(1, 10, step=2)
assert i._max == 10 and i._step == 2 and i._min == 1


def test_value_error(*args, **kwargs):
    try:
        i = Integer(*args, **kwargs)
    except ValueError:
        pass
    else:
        raise AssertionError

test_value_error(10, max=1)
test_value_error(1, 10, min=1)
test_value_error(1, 10, 2, step=1)
test_value_error(1, 10, 2, step=1, min=1, max=1)
# Arguments test

to_ten = Integer(10)

all_values = [x for x in to_ten]

assert x == 9
assert all_values == range(10)

odd_num = Integer(1, 11, 2)
assert range(1, 11, 2) == [x for x in odd_num]

even_num = Integer(0, 11, 2)
assert range(0, 11, 2) == list(even_num)

endless_num = Integer()
max_ = 100
for x in endless_num:
    if x >= max_:
        break
assert x == max_

for i in range(max_):
    x = endless_num.previous()

assert x == 0 and i == (max_-1)
