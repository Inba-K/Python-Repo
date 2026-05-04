import array as arr
a=arr.array('i',[0,1,1,0,0,0,1,1])
yeehaw=int(input("What number do you want to flip to? "))
if yeehaw==0:
    flip=0
    for i in range(len(a)):
        if a[i]==1:
            flip+=1
            a[i]=0
    print("Number of flips needed:",flip)
    print(a)

if yeehaw==1:
    flip=0
    for j in range(len(a)):
        if a[j]==0:
            flip+=1
            a[j]=1
    print("Number of flips needed:",flip)
    print(a)
