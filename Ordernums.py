import array as arr
a=arr.array('i',[1,2,1,2,0,2,1,0,1,2,0,0])
for i in range(len(a)):
    if a[i]==0:
        a.append(0)
        a.remove(a[i])
for j in range(len(a)):
    if a[j]==1:
        a.append(1)
        a.remove(a[j])
for k in range(len(a)):
    if a[k]==2:
        a.append(2)
        a.remove(a[k])
print(a)
