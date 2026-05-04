import array as arr
a=arr.array('i',[1,3,2,4,5])
b=arr.array('i',sorted(a))
print("The smallest element is",b[0])
print("The greatest element is",b[len(b)-1])
