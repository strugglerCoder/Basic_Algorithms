# "abc" => "cba"

def reverse(string):
    revstring = ""
    for s in string:
        revstring = s + revstring
    return revstring

print("By logic 1:",reverse("abc"))

def reverse1(string):
    temp = ""

    i=len(string)
    while(i>0):
        a = (i-1)%10
        temp = temp + string[a]
        i-=1
    return (temp)

print("By logic 2:", reverse1("123456789"))
