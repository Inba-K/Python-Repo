num=int(input("Enter a number:"))
c=[]
for x in range(num):
    if x**2==num:
        c.append(x)
if len(c)>=1:
    print(num,"is a power of 2.")
else:
    print(num,"isn't a power of 2.")
