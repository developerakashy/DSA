def remove_duplicates(arr):
    temp_arr = [0] * len(arr)
    temp_arr[0] = arr[0]
    ind = 1

    for i in range(1,len(arr)):
        if temp_arr[ind-1] != arr[i]:
            temp_arr[ind] = arr[i]

            ind += 1

    for j in range(ind):
        arr[j] = temp_arr[j]

    return ind

arr = [10,10,10,20,20,20]
print("Unique Elements:",remove_duplicates(arr))


def rem_duplicates(arr):
    ind = 1
    for i in range(1,len(arr)):
        if arr[ind-1] != arr[i]:
            arr[ind] = arr[i]

            ind += 1

    return ind

arr1 = [10,20,20,30,30,30,30,30]
print("Efficient unique Elements:",rem_duplicates(arr1))

    