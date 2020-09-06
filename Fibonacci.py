# 0 1 1 2 3 5 8 13 21 34 55 ...
def Fibonacci(Range):
    t1 = 0
    t2 = 1

    if Range == 0:
        print(t1,end=" ")
    elif Range == 1:  # fkt if takun bgha ani input 0 dya, ts ka hot?
        print(t2,end=" ")
    else:
        for i in range(2, Range + 1):
            t3 = t1 + t2
            t1 = t2
            t2 = t3
        print(t3, end=" ")

Range = int(input("Enter range for Fibonacci series : "))
for i in range(Range):
    Fibonacci(i)
