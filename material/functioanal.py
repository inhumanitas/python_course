
iterable = [0, 1, 2, 3, 4]
print 'all', not all(iterable)
print 'any',  any(iterable)

bool(iterable)
if not iterable:
    print 'empty'


def summ(item):
    return item+1

print map(summ, iterable)

print any(map(lambda x: x > 1, iterable))


lst = (0, 1, 2, 3, 4, 5, 6, 0)

print filter(lambda x: x > 3, lst)
print filter(bool, lst)

lst2 = sorted(lst)
print lst is lst2

print sum(lst)


# ------------------------------------------------------------------------

reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])  # ((((1+2)+3)+4)+5)


assert sum(lst) == reduce(lambda x, y: x + y, lst)
assert all(lst) == reduce(lambda x, y: x and y, lst)  # all
assert any(lst) == reduce(lambda x, y: x or y, lst)  # any

# assert max(lst) == reduce(lambda x, y: x, lst)  # max

reduce(max, lst)

reduce(lambda x, y: x + [y], 'abc', [])


# ------------------------------------------------------------------------
#  visibility

glob = 123


def fn():
    return glob + 123

assert glob+123 == fn()
assert glob == 123


def fn():
    glob = 1
    return glob + 123

assert glob+1 == fn()
assert glob == 123


def fn(glob):
    return glob + 123

assert glob+123 == fn(glob)
assert glob == 123


def fn():
    global glob
    glob += 123

fn()

assert glob == 123+123


glob = 123


def outer():
    glob = 1

    def fn():
        global glob
        glob += 123
        return glob
    return fn()

assert glob+123 == outer()


functions = [lambda x: x+n for n in range(10)]

assert functions[2](2) == 9 + 2
assert functions[4](2) == 9 + 2



functions = [(lambda m: lambda x: x+m)(n) for n in range(10)]

assert functions[2](2) == 2 + 2
assert functions[4](2) == 4 + 2


# ------------------------------------------------------------------------
# collections
assert zip('abcsdfsadfasdf', [1, 2, 3]) == [('a', 1), ('b', 2), ('c', 3)]


import itertools

slice = itertools.islice(xrange(100000000000), 10000, 10200, 50)

print slice # <itertools.islice object at 0x7f54a3f3dba8>

l = []
for num in slice:
    l.append(num)

assert l == [10000, 10050, 10100, 10150]

# tee(iterable, n=2)
# chain(*iterables)

# combinations
# list(itertools.combinations([1,2,3,4], 2))
# [[1,2], [1,3], [1,4], [2,3], [2, 4], [3,4]]

# compress
# list(itertools.compress('абвгде', [1,0,0,0,1,1]))
# ['а', 'д', 'е']

# dropwhile

# def func(x):
#     return x > 3
# list(itertools.dropwhile(func, [4, 5, 6, 0, 7, 2, 3]))
# [0, 7, 2, 3]
# def func():
#         return x > 3
# list(itertools.takewhile(func, [4, 5, 6, 0, 7, 2, 3]))
# [4, 5, 6]

# cycle

# ifilter
# imap

# izip
# list(itertools.zip_longest((1,2,3), [4]))
# [(1, 4), (2, None), (3, None)]


# ----------------------------------------------------------------------------
import collections

Point = collections.namedtuple('Point', 'x y')
# Point.__doc__  # докстринг нового класса

p = Point(11, y=22)
p[0] + p[1]

# collections.defaultdict
# collections.Ordereddict

