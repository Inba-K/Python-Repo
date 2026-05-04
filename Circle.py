import array as arr

a=arr.array('i',[8,-1,3,4])

current_sum=0
max_sum=0
min_sum=0

for i in range(len(a)):
    current_sum+=a[i]
    max_sum=max(max_sum,current_sum)
    if current_sum<0:
        current_sum=0

current_sum=0

min_sum=float('inf')
for k in a:
    current_sum=min(k,current_sum+k)
    min_sum=min(min_sum,current_sum)
print(max_sum,min_sum)
