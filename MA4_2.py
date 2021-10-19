#!/usr/bin/env python3
# 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
import time
import matplotlib
import matplotlib.pyplot as plt
from integer import Integer

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))
            
length = [x for x in range(10)] #till tid 45

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
        
    plt.plot(length,fib_py_time)
    plt.plot(length,fib_cpp_time) # do your plotting here
    plt.savefig("fibonacci.png")
    plt.show()
    #f = Integer(47) #Integer(47) blir negativt pga overflow, max-värde har nåtts!
    #print(f.fib())
    
if __name__ == '__main__':
   main()


