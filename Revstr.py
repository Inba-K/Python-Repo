def rev_str(n):
    if len(n)<=1:
        return n
    return rev_str(n[1:])+n[0]
print(rev_str("Inba"))
