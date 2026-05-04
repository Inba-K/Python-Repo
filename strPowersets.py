def power_set(string):
    n=len(string)
    result=[]
    for i in range(1<<n):
        subset=[]
        for j in range(n):
            if i &(1<<j):
                subset.append(string[j])
        result.append(subset)
    print(result)
power_set("anki")
