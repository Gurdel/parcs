# import gmpy2
from Pyro4 import expose
from random import randint
import random

def func(s):
    buf = list(map(float, s.split()))
    n = int(buf[0])
    A = buf[1:n+1]
    B = buf[n+1]
    x = buf[n+2:n+n+2]
    y = buf[n+n+2:]
    sx = sum([x[i] * A[i] for i in range(n)])
    sy = sum([y[i] * A[i] for i in range(n)])
    dB = 0.0001
    if((sx <= B + dB and sx >= B - dB) and (sy <= B + dB and sy >= B - dB)):
        b = y
        a = [x[i] - b[i] for i in range(n)]

        res = ''
        for i in range(n):
            res += str(int(A[i])) + '*A' + str(i) + '+'
        res += ' = ' + str(int(B)) + ' ---> '
        for i in range (n):
            res += 'x' + str(i) + '=' + str(a[i]) + '*t+' + str(b[i]) + ' '
        return res
    return ''

class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers
        print("Inited")

    def solve(self):
        print("Job Started")
        print("Workers %d" % len(self.workers))

        arr = self.read_input()
        step = int(len(arr) / len(self.workers))

        mapped = []
        for i in xrange(0, len(self.workers)):
            mapped.append(self.workers[i].mymap(([i for i in arr[i * step:i * step + step]])))
        self.write_output(mapped)

    @staticmethod
    @expose
    def mymap(a):
        res = []
        for el in a:
            buf = func(el)
            if (buf != ''):
                res.append(buf)
        return res

    @staticmethod
    @expose
    def myreduce(mapped):
        print("reduce")
        output = []

        for primes in mapped:
            print("reduce loop")
            output = output + primes.value
        print("reduce done")
        return output

    def read_input(self):
        f = open(self.input_file_name, 'r')
        lines = [line.rstrip('\n') for line in f]
        f.close()
        return lines

    def write_output(self, output):
        f = open(self.output_file_name, 'w')
        for a in output:
            for i in a.value: f.write(str(i) + '\n')
        f.close()
        print("output done")