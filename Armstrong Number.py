def order(number):
    n = 0
    while (number != 0):
        n += 1
        number = number // 10
    return n


def armstrong(number):
    temp = number
    sum = 0
    power = order(temp)
    while (temp != 0):
        r = temp % 10   
        sum = sum + r ** power
        temp = temp // 10

    if (sum == number):
        print(number, "is a armstrong number")
    else:
        print(number, "is not armstrong number")


n = int(input("Enter number to check armstrong or not : "))
armstrong(n)