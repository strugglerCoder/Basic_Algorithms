def sort(arr):
    temp = 0

    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

    print(arr)

arr = [3,2,1]
sort(arr)
