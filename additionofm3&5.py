# output => ab\\\\nc
# abc "pqr" xyz

# a,b = input("enter no for add (give space between them) :").split()
# x = int(a)
# y = int(b)
# a=int(input("enter 1st no. :"))
# b=int(input("enter 2nd no. :"))
# print(x+y)

# string = 'abc "pqr" xyz'
# print(string)
# for i in string:

# print(string)

n = input("enter a no : ")
number = int(n)
addition = 0
for i in range(number):
    if i%3==0 or i%5==0:
        print(i)
        addition = addition+i
print("addition is : "+str(addition))




