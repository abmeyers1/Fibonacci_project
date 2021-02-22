"""
Alex Brumfield-Meyers
2/22/2021

Project - Fibonacci finder
Requests integer from user, returns n-th number in fibonacci sequence.
Determines time in takes to calculate sequence up to n-th integer
Requires Time

"""

from time import time


def fib_find():
    n = int(input('Please enter a positive integer: \n'))
    print(f"Finding {n}th term of fibonacci sequence")
    fibs = [0, 1]
    if n < 3:
        return fibs[n-1]
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    print(fibs)
    return fibs[-1]


t1 = time()
print(fib_find())
print(f"Finished calculating in {time() - t1} seconds")
