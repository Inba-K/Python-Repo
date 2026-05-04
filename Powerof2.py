def power_2(n):
    if n==1:
        return "True"
    if n<=0 or n%2!=0:
        return 0
    return power_2(n//2)
print(power_2(8))
