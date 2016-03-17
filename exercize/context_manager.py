# coding: utf-8

# 1
"""
    Реализовать контекстный менеджер такой же как open,
    но с проверкой на наличие файла
    т.е. если файла нет то конструкция не должна падать с ошибкой

    with MyOpen('wrong_file_path') as fh:
        fh.readlines()
"""
import os


class MyOpen(object):
    def __init__(self, file_name, mode='r'):
        self.file, self.mode = file_name, mode

    def __enter__(self):
        # create file if there is no one
        if not os.path.isfile(self.file):
            fh = open(self.file, 'w')
            fh.close()

        self.fh = open(self.file, self.mode)
        return self.fh

    def __exit__(self, type, value, traceback):
        self.fh.close()
