x = 0
for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        x += i
        print(x)

def f(upperbound):
    hassenfeffer = 0
    for gobbledygook in range(upperbound):
        if gobbledygook%3 == 0 or gobbledygook%5 == 0:
            hassenfeffer += gobbledygook
            print(hassenfeffer)

input("\n\nPress the enter key to exit.")
