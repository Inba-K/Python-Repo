a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
b1=b
ans=0
while b<=a:
    b+=b1
    ans+=1
remain=a-b+b1
print(f"The quotient is {ans} with a remainder of {remain}.")
