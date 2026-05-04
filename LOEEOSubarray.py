import array as arr
a=arr.array('i',[1,2,4,6,7,8])
thing=0
num=0
for i in range(len(a)):
    thing=a[i]
    if thing%2==0 and a[i]%2!=0:
        num+=1

num=0

for j in range(len(a)):
    thing=a[j]
    if thing%2!=0 and a[j]%2==0:
        num+=1
print(num)
