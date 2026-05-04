def reverse_number(n):
    if n<10:
        return n
    digits=len(str(n))
    return (n%10)*(10**(digits-1))+reverse_number(n//10)
n=123
print(reverse_number(n))
