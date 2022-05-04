from math import factorial

def loops(number):
    n = 0
    for i in range(number):
        r = 0
        _str = ""
        for j in range(i + 1):
            output = factorial(n) // (factorial(r) * factorial(n-r))
            _str = _str + str(output) + " "
            r += 1
        n += 1
        print(_str)

loops(int(input("Enter Number: ")))