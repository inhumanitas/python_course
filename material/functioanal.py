
iterable = [0, 1, 2, 3, 4]
print 'all', not all(iterable)
print 'any',  any(iterable)

bool(iterable)
if not iterable:
    print 'empty'


def summ(item):
    return item+1

print map(summ, iterable)

print any(map(lambda x: x>1, iterable))


lst = (0, 1, 2, 3, 4, 5, 6, 0)

print filter(lambda x: x>3, lst)
print filter(bool, lst)

lst2 = sorted(lst)
print lst is lst2

print sum(lst)
