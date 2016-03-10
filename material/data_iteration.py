# coding: utf-8

# ---------------------------------------------------------------------------
# Iterator
# list iteration

for el in [1, 2, 3, 4, 5]:
    print el

lst = range(5)
lst_iterator = xrange(5)
print lst, lst_iterator


class SimpleIterator(object):
    __curitem = 0

    def __iter__(self):
        return self

    def next(self):
        self.__curitem += 1
        if self.__curitem > 5:
            raise StopIteration()

        return self.__curitem


for i in SimpleIterator():
    print 'i = ', i


class DataHandler(object):
    def __init__(self, iterable):
        super(DataHandler, self).__init__()
        self.__iterable = iterable
        self.__cur_position = 0
        self.__high = len(iterable)

    def next(self):
        if self.__cur_position >= self.__high:
            raise StopIteration()

        value = self.__iterable.__getitem__(self.__cur_position)
        self.__cur_position += 1
        return value


class Iterable(object):

    def __init__(self, data):
        super(Iterable, self).__init__()
        self.data = data

    def __iter__(self):
        return self.data


for i in Iterable(DataHandler([1, 2, 3, 4])):
    print i,
print

for i in Iterable(DataHandler(range(10))):
    print i,
print
