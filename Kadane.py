import array as arr
a=arr.array('i',[-2,1,-3,4,-1,2,1])
current_sum=0
max_sum=0
for i in range(len(a)):
    current_sum+=a[i]
    max_sum=max(max_sum,current_sum)
    if current_sum<0:
        current_sum=0
print(max_sum)
