def sum_el(arr):
    if len(arr)==0:
        return 0
    return arr[0]+sum_el(arr[1:])
print(sum_el([1,2,3]))
