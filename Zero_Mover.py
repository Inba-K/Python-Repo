import array as arr
a=arr.array('i',[1,5,0,5,0,3,0,0,123,165])
for i in range(len(a)):
    if a[i]==0:
        a.append(0)
        a.remove(a[i])
print(a)
