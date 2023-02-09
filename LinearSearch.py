def Search(list,no):
    if no in list:
        print("no is there")
        print(list)
    else:
        print("no is not there")
        print(list)

no = int(input("Enter no to search by normal method : "))
Search([1,2,3,4,5],no)

pos = 0

def linear(list,key):

    i = 0
    while (i<len(list)):
        if key==list[i]:
            globals()["pos"]=i+1
            return True
        i+=1
    return False

no = int(input("enter no to seach by Linear Searching :"))
sort = linear([7,6,4,2,9,8,1,3,5,2],no)

if sort==True:
    print(no, "is found at", pos)
else:
    print(no,"is not found in list")
