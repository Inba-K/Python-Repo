import array as arr
a=arr.array('i',[3,6,2,2,6,1,0,9])
target=10
for i in range(len(a)):
    current_sum=0
    for j in range(i,len(a)):
        current_sum+=a[j]
        if current_sum==target:
            print(a[i:j+1])
