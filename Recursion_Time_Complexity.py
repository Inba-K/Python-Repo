import time

def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)

def print1to10(n):
    if n==10:
        return 10
    else:
        print(n)
        return print1to10(n+1)

n=int(input("Enter a number: "))

start=time.time()
print(fac(n))
print(print1to10(n))
end=time.time()
print(f"Time taken: {round(end-start,8)} seconds")
