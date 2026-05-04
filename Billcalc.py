def money(n):
    result=[]
    def sort(n,path):
        if n==0:
            result.append(path.copy)
            return
        if n<0:
            return
        if n%500==0:
            path.append(n-500)
            sort(n,path)\
            print(path)
            path.pop()
        if n%100==0:
            path.append(n/100)
            sort(n-n/100,path)
            path.pop()
        if n%10==0:
            path.append(n/10)
            sort(n-n/10,path)
            path.pop()
        if n%5==0:
            path.append(n/5)
            sort(n-n/5,path)
            path.pop()
        path.append(n)
    sort(n,[])
    return result
print(money(1000))
