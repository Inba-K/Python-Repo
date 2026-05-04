def negative(n):
    if n == -2:
        return
    print(n)
    negative(n - 1)

x = int(input("Enter a number: "))
negative(x)
