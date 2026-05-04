def parenthesis(n):
    result=[]
    def pair_parenthesis(open_count,close_count,path):
        if open_count==n and close_count==n:
            result.append(path)
            return
        if open_count<n:
            pair_parenthesis(open_count+1,close_count,path+"(")
        if close_count<open_count:
            pair_parenthesis(open_count,close_count+1,path+")")
    pair_parenthesis(0,0,"")
    return result
print(parenthesis(3))
