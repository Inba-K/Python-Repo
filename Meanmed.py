import array as arr
a=arr.array('i',[4,3,2,1,5])
b=0
for i in range(0,len(a)):
    b+=a[i]
print(b/len(a))
c=arr.array('i',sorted(a))
if len(a)%2==0:
    median=c[(len(a)//2)-1]
    print(median)
else:
    median=c[len(a)//2]
    print(median)
