def power_4(n):
    if n==1:
        return 1
    if n<=0 or n%4!=0:
        return 0
    return power_4(n//4)
print(power_4(4))
