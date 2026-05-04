def letterCombination(digits):
    if not digits:
        return []
    keypad={'2':'ABC','3':'DEF','4':"GHI",'5':"JKL",'6':"MNO",'7':"PQRS",'8':'TUV','9':'WXYZ'}
    result=[]
    def backtrack(index,path):
        if index==len(digits):
            result.append(path)
            return
        for ch in keypad[digits[index]]:
            backtrack(index+1,path+ch)
    backtrack(0,"")
    return result
print(letterCombination("322"))
