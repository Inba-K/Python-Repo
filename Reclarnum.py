def largest_el(arr):
    if len(arr)==1:
        return arr[0]
    max1=largest_el(arr[1:])
    if arr[0]>=max1:
        return arr[0]
    else:
        return max1

print(largest_el([1,2,3,4,5]))
