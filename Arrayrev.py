import array as arr
a=arr.array('i',[1,2,3,4,5,6])
print("The original array is",a)
n=(len(a))-1
while n>=0:
    a.append(a[n])
    a.remove(a[n])
    n-=1
print("The reversed array is",a)
