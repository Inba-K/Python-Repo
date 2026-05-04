num=int(input("Enter a number: "))
n=num
if n>0 and (n&(n-1))==0 and (n&7)==0:
    while num>1:
        n>>=3
print(num)
