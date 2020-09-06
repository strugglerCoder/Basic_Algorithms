pos = 0


def binary(list, key):
    lower = 0
    upper = len(list) - 1

    while (lower <= upper):
        mid = (lower + upper) // 2

        if list[mid] == key:
            globals()['pos'] = mid + 1
            return True
        else:
            if key < list[mid]:
                upper = mid - 1
            else:
                lower = mid + 1

    return False


# ########## list should be sorted ####################

list = [2, 13, 24, 36, 57]
list2 = [5, 7, 8, 4, 2, 3, 1]

z = sorted(list2)

list.reverse()
list.reverse()

print(list)
print(z)
key = int(input("Enter no to find by binary Search : "))
search = binary(list, key)
search2 = binary(z, key)

if search == True:
    print(key, "found at position", pos)
else:
    print(key, "not found")

if search2 == True:
    print(key, "found at position", pos)
else:
    print(key, "not found")
