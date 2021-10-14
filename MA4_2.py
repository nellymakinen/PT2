#!/usr/bin/env python3

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
# from integer import Integer

def fib_py(n):
        if n <= 1:
            return n
        else:
            return(fib_py(n-1) + fib_py(n-2))
        
def main():
    #f = Integer(5)
    #print(f.get())
    #f.set(7)
    #print(f.get())
    print(fib_py(7))
    plt.plot([1,2,3],[1,2,3]) # do your plotting here
    plt.savefig("fibonacci_timing.png")
    #f = Integer(n)
    #f.fib()
    
if __name__ == '__main__':
    main()
