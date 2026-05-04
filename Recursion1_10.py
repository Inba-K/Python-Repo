def order(n):
    if n==10:
        return 10
    else:
        print(n)
        return order(n+1)
print(order(1))
