import array as arr
a=arr.array('i',[1,0,0,1,1,1,0,1,1])
max_count=0
current=0
c=arr.array('i',[])
for i in a:
    if i==1:
        current+=1
        max_count=max(max_count,current)
    else:
        current=0
print(max_count)
