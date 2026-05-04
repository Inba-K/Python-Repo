a=[1,2,3]
def steps(n):
    if n<0:
        return 0
    return 1+(steps())
