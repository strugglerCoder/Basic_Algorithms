def sort(lists):
    count = 0
    for i in range(len(lists)-1):
        if lists[i] > lists[i+1]:
            return False        # as ka? true chi cond eth ka ny?
    return True

print(sort([1,2]))

