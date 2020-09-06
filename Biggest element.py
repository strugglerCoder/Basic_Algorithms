# [10,20,30,40] => 40
# [10,5,20,30,15,35] => 35

def biggest(lists):
    big = lists[0]
    i = 1
    while i < len(lists):
        if big < lists[i]:
            big = lists[i]
            i = i + 1
        else:
            i += 1
    return big


print(biggest([10, 250, 30, 40]))
print(biggest([10000, 5, 100, 30, 35, 15]))
