import array as arr
a=arr.array('i',[1,2,3,52,357,3,4,8,2,7])
b=arr.array('i',sorted(a))
n=len(b)-1
while n>=0:
    b.append(b[n])
    b.remove(b[n])
    n-=1
print(b[0])
