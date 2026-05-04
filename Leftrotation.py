import array as arr
a=arr.array('i',[1,2,3,4,5])
n=int(input("Enter the number of left rotations: "))
while n>0:
    a.append(a[0])
    a.remove(a[0])
    n-=1
    print(a)
