import math

def f(n):
    x = 0
    y = 0
    for i in range(1,math.factorial(n+1)):
        if i%n == 0:
            print(i)
            break

