def lettercount(string, letter):
    l_count = 0

    for i in string:
        if i == letter:
            l_count += 1

    print(l_count,letter)


string = "aaabbcadd"
print(string)
l = input("Enter a letter which you want to see count of that : ")
lettercount(string, l)
