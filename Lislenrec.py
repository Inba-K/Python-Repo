def len_arr(arr):
    if len(arr)==0:
        return 0
    max1=len_arr(arr[1:])
    return 1+max1
print(len_arr([1,2,3]))
