# coding: utf-8

"""
Working with classes
"""

import os


type(type)  # type


class OldStyle:
    """
    Classic style class
    """
    var = None  # class variable
    _var = None  # class protected variable
    __var = None  # class private variable

    def __init__(self):
        self.var = 'OldStyle'  # instance variable

    def method1(self):
        """Class method"""
        return self.var

    def _protected_method(self):
        """Class method"""
        return self.var

    def __private_method(self):
        """Class method"""
        return self.var


class NewStyle(object):
    """
    New style class
    """
    var = None

    def __init__(self):
        self.var = 'NewStyle'


old1_instance = OldStyle()
new1 = NewStyle()

print 'OldStyle', type(OldStyle), dir(old1_instance)
print 'NewStyle', type(NewStyle), dir(new1)


class MultiInheritance(NewStyle, OldStyle):
    pass


# ---------------------------------------------------------------------------
# resolving vars
class Class1(object):  # Класс нового стиля
    var = u"Это значение в классических классах"
# #
# class Class1:  # Классический класс
#     var = u"Это значение в классических классах"

class Class2(Class1): pass
class Class3(Class2): pass
class Class4(Class3): pass

class Class5(Class2):
    var = u"Это значение в классах нового стиля"

class Class6(Class5): pass
class Class7(Class4, Class6): pass

c1 = Class7()
print c1.var


# ---------------------------------------------------------------------------
# dynamic assignment
class A(object):
    pass


a_instance = A()
assert not hasattr(a_instance, 'var')


A.var = 'A_var'
assert hasattr(a_instance, 'var')


a_instance = A()
def fn(self): pass
A.fn = fn
assert hasattr(a_instance, 'fn')
print fn, A.fn, a_instance.fn


# ---------------------------------------------------------------------------
# class variable visibility, class creation
class BaseObject(object):

    def __new__(cls, *args, **kwargs):
        print 'creating object'
        cls_parents = super(BaseObject, cls).__new__(cls, *args, **kwargs)
        return cls_parents

    def __init__(self):
        self.var = 1
        print 'object initialized'

    def __del__(self):
        print 'object destroyed'

# BaseObject.var
b_obj = BaseObject()
b_obj.var = 3
b_obj2 = BaseObject()
b_obj.var  # 1


class VM(BaseObject):
    """
    VM object
    Supported stop\start\pause
    """
    name = None
    # TODO state can be separated from VM object
    _state = None  # current VM state

    # all available states
    __states = {
        'STOPPED': 0,
        'RUN': 1,
        'PAUSED': 2,
    }

    def __init__(self, name, flavour_id):
        super(VM, self).__init__()
        self.name = name
        self.flavour_id = flavour_id

    def stop(self):
        self._state = self.__states['STOPPED']
        return self._state

    def start(self):
        self._state = self.__states['RUN']
        return self._state

    def pause(self):
        self._state = self.__states['PAUSED']
        return self._state

# instance
vm1 = VM('test_ubuntu', 1)
# method call
vm1.name = 'test_ubuntu'

vm1.pause()
assert vm1._state == 2


assert isinstance(vm1, BaseObject)

s = 'abcdef'  # str
us = u'abcdef' # unicode

print 'isinstance(s, str), isinstance(s, unicode), isinstance(s, basestring)'
print isinstance(s, str), isinstance(s, unicode), isinstance(s, basestring)

print 'isinstance(us, str), isinstance(us, unicode), isinstance(us, basestring)'
print isinstance(us, str), isinstance(us, unicode), isinstance(us, basestring)

assert issubclass(VM, object)
VM.__bases__
VM.__class__, VM.__dict__
vm2 = vm1.__class__('vm2', 2)

# ---------------------------------------------------------------------------
# classmethod, staticmethod


class Path(object):

    prefix = 'tnx'
    @classmethod
    def cwd2(cls):
        pass

    @classmethod
    def cwd(cls):
        cls.cwd2()
        return os.path.curdir

    @staticmethod
    def normalize(path):
        return os.path.normpath(path)

    def append(self, path):
        return self.prefix + path


cur = Path.cwd()
path = '///root//tmp/'
norm_path = Path.normalize(path)
prefix_path = Path.append(Path(), path)


# ---------------------------------------------------------------------------
# more magic
class Magic(BaseObject):
    x = 1
    def __len__(self):
        return 1

    def __getattribute__(self, name):
        return self.x  # super(Magic, self).__getattribute__(name)

    def __getattr__(self, item):
        """Invoked if the attribute wasn't found the usual ways. Eg Magic.x"""

    def __getitem__(self, item):
        """Act like dictionary. Eg Magic['x']"""

    def __get__(self, instance, owner):
        """Descriptor method """

    def __repr__(self):
        """The goal is to be unambiguous """
        return super(Magic, self).__repr__()

    def __str__(self):
        """The goal is to be readable """
        return super(Magic, self).__str__()

    def __add__(self, other):
        pass

    def __cmp__(self, other):
        pass

    def __call__(self, *args, **kwargs):
        pass


class Point(object):
    def __init__(self, x, y):
        super(Point, self).__init__()
        self.x, self.y = x, y

    def __repr__(self):
        return u"Point({x}, {y})".format(x=self.x, y=self.y)


p = Point(3, 55)


class Ten(object):
    def __getitem__(self, item):
        if item < 10:
            return 10 + item
        raise IndexError()


for i in Ten():
    print i


# ---------------------------------------------------------------------------
# property, show get, set methods!!!!

class SomeObject(object):
    var = None

so_instance = SomeObject()
so_instance.__dict__  # {}
SomeObject.__dict__  # {'var': None, '__dict__': <attribute '__dict__' of 'SomeObject' objects>, '__module__': '__main__', '__weakref__': <attribute '__weakref__' of 'SomeObject' objects>, '__doc__': None}

so_instance.var = 'set value'
so_instance.__dict__  # {'var': 'set value'}
# so_instance.no_var  # AttributeError


class C(object):

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


c = C()
c.x = 1
c.__dict__  # {'_x': 1}


class StateMixin(object):
    _state = None  # current VM state
    STOPPED = 0
    # all available states
    __states = {
        'STOPPED': STOPPED,
        'RUN': 1,
        'PAUSED': 2,
    }

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value


class NewVM(BaseObject, StateMixin):  pass
nvm = NewVM()
print nvm.state
nvm.state = 1

# ---------------------------------------------------------------------------
# meta introduction
isinstance(object, type)  # True


class A(object):
    pass


def class_creator():
    class A(object):
        pass

    return A


type('A', (object, ), {})


# ---------------------------------------------------------------------------
# define meta
class Ameta(type):

    def foo(cls):
        print 'Ameta.foo'


class AA(object):
    __metaclass__ = Ameta

AA.foo()
a_instance = AA()

# a_instance.foo


# ---------------------------------------------------------------------------
# decorators

import time

def timer(func):
    def tmp(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print "Время выполнения функции: %f" % (time.time()-t)
        return res

    return tmp


@timer
def dec_func(x, y):
    return x + y

dec_func(1, 2)  # Время выполнения функции: 0.0004


def func(x, y):
    return x + y


timer(func)(1, 2)  # # Время выполнения функции: 0.0004


def dec(logfile):
    def wrapper1(fn):
        def wrapper(*args, **kwargs):
            print 'Openned'
            res = fn(*args, **kwargs)
            print logfile, 'closed and writted'
            return res
        return wrapper
    return wrapper1


@dec("/tmp/main.log")
def main(tmp):
    print tmp


@dec("/tmp/summator")
def summator(tmp):
    print tmp

# ---------------------------------------------------------------------------
