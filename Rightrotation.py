import array as arr
a=arr.array('i',[1,2,3,4,5])
print("The original array is",a)
n=int(input("Enter the number of right rotations: "))
for i in range(n):
    a.insert(0,a[len(a)-1])
    a.pop()
    print(a)
