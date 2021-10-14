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
        
length = [x for x in range(35)]

fib_py_time = []
fib_cpp_time = []

for i in length:
    ts = time.time()
    fib_py(i)
    f = Integer(i)
    f.fib()
    fib_py_time.append(time.time() - ts)
    fib_cpp_time.append(time.time() - ts)
    
plt.plot(length, fib_py_time, length, fib_cpp_time)
plt.show()

def main():
    
    print(fib_py(7))
    #plt.plot([1,2,3],[1,2,3]) # do your plotting here
    plt.savefig("fibonacci_timing.png")
    f = Integer(5)
    print(f.fib())
    
if __name__ == '__main__':
    main()
