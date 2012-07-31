def f(n):
   ftotal = 0
   fsubtotal = 0
   gtotal = 0
   gsubtotal = 0
   gtotalsq = 0
   diff = 0
   for i in range(n):
       fsubtotal += i**2
       ftotal = fsubtotal + n**2
       gsubtotal += i
       gtotal = gsubtotal + n
       gtotalsq = gtotal**2
       diff = gtotalsq - ftotal
       print(diff)

n = int(input("Find the difference between the sum of the squares of the first \
n natural numbers and the square of the sum.  Define n as:"))

f(n)

input("\n\nThe bottom number is the solution.\nPress the enter key to exit.")
