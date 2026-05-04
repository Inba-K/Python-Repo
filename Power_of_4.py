num=int(input("Enter a number: "))
if num>0 and (num&(num-1))==0 and (num&0xAAAAAAAA)==0:
    print(num, "is a power of 4.")
else:
    print(num, "isn't a power of 4.")
