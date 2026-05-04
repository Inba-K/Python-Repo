import array as arr
a=arr.array('i',[150,200,148,160,223,171,143])
n=0
for i in range(0,len(a)-1):
    if a[i+1]>a[i]:
        n+=a[i+1]-a[i]
print(n)
