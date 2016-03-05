# coding: utf-8

"""
    Preferred way to run main program
"""

from os.path import isdir
from material.data_types.types_tryout import fn_sum


def main():
    isdir('/path')
    print fn_sum(3)
    print 'run server'


if __name__ == '__main__':
    main()
