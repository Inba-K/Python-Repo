import array as arr
a=arr.array('i',[-4,6,2,0,0,1,1])
for i in range(len(a)):
    left_sum=0
    right_sum=0
    for j in range(i):
        left_sum+=a[j]
    for k in range(i+1,len(a)):
        right_sum+=a[k]
    if left_sum==right_sum:
        print(i)
