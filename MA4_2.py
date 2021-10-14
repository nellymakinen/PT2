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
            
length = [x for x in range(15)]

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
        
    #print(fib_cpp_time)
    #print(fib_py_time)
    #plt.plot(length,fib_py_time)
    #plt.plot(length,fib_cpp_time)
    #fig, axs = plt.subplots(2)
    #fig.suptitle('Fibonacci timing')
    #axs[0].plot(length, fib_py_time)
    #axs[1].plot(length, fib_cpp_time)
    
    #print(fib_py(7))
    plt.plot(length,fib_py_time,fib_cpp_time) # do your plotting here
    plt.savefig("fibonacci_time.png")
    plt.show()
    #f = Integer(5)
    #print(f.fib())
    
if __name__ == '__main__':
    main()
