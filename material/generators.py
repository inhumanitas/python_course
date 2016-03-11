# coding: utf-8

"""
    Generator object
"""

for i in [1, 3, 6]:
    # print i
    pass


def generator(max=10):
    i = max
    while True:
        print 'before'
        yield i
        print 'after'
        i -= 1
        if i <= 0:
            break
#
# for i in generator(20):
#     print i


def coroutine():
    i = 10

    while True:
        print 'before'
        val = (yield)
        print 'val', val
        val1 = (yield)
        print 'val1',  val1
        i -= 1
        if i <= 0:
            i = 10

c = coroutine()
print c.next()
print c.send(0)
print c.send(2)
print c.send(3)

