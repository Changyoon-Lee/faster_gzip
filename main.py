# This is a sample Python script.
import time, gzip
from subprocess import Popen, PIPE
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess, io, sys
import functools
def gziplines(fname):

    f = Popen(['zcat',fname],stdout = PIPE)
    # for i in io.BytesIO(f.communicate()[0]):
    #     yield i
    for line in f.stdout:
        yield line.decode('utf-8')


# Press the green button in the gutter to run the script
if __name__ == '__main__':
    fname='test.gzip'
    start = time.time()
    for line in gziplines(fname):
        a = line.strip().replace('-','0').split('\t')

    end = time.time()
    print('zcat : ', end-start)
    start = end

    with gzip.open(fname, 'rb') as gz:
        with io.TextIOWrapper(io.BufferedReader(gz)) as fr:
            for line in fr:
                a = line.strip().replace('-', '0').split('\t')

    end = time.time()
    print('gzip : ', end - start)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
