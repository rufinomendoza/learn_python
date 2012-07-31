def f(n):
    total = 0
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
        if a < n and a%2 == 0:
            total += a
            print(total)

n = int(input("By considering the terms in the Fibonacci sequence whose values do not \
exceed 'n,' find the sum of the even-valued terms.  Define n as:"))

f(n)

input("\n\nThe bottom number is the solution.\nPress the enter key to exit.")
