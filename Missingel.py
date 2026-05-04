import array as arr
a=arr.array('i',[3,1,6,4,2])
b=arr.array('i',[1,2,3,4,5,6])

n=len(a)-1
o=len(b)-1

x=0
while n>=0:
    x+=a[n]
    n-=1

y=0
while o>=0:
    y+=b[o]
    o-=1
print("The missing element is",y-x)
