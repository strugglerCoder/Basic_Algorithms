#[10,20,10,30,10] => 10/3

def occurrence(list, no):
    inc = 0
    for i in list:
        if no==i:
            inc+=1
    return inc

print(occurrence([10,20,10,30,10,20], 10))
print(occurrence([10,20,10,30,10,20], 20))
print(occurrence([10,20,10,30,10,20], 30))

