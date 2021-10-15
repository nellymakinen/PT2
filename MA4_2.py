#!/usr/bin/env python3
import time
import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
from integer import Integer

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))
            
length = [x for x in range(20)]

fib_py_time = []
fib_cpp_time = []

def main():
    for i in length:
        ts = time.time()
        fib_py(i)
        fib_py_time.append(time.time() - ts)
        
    for i in length:
        ts = time.time()
        f = Integer(i)
        f.fib()
        fib_cpp_time.append(time.time() - ts)
        
    plt.plot(length,fib_py_time ,fib_cpp_time) # do your plotting here
    plt.savefig("fibonaccitiming.png")
    plt.show()
    #f = Integer(47)
    #print(f.fib())
    
if __name__ == '__main__':
    main()
