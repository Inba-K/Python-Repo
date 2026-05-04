num=int(input("Enter a number"))
binary_result=''
if num==0:
    binary_result=0
else:
    while num>0:
        remainder=num%2
        binary_result=str(remainder)+binary_result
        num=num//2
rev_binary_result=binary_result[::-1]
rev_decimal=int(rev_binary_result)
print(rev_decimal)
