def power_set(nums):
    n=len(nums)
    result=[]
    for i in range(1<<n):
        subset=[]
        for j in range(n):
            if i &(1<<j):
                subset.append(nums[j])
        result.append(subset)
    print(result)
power_set("567")
