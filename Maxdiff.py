import array as arr
a=arr.array('i',[4,5,234,2,6,82,234,5234])
b=arr.array('i',sorted(a))
print(b[len(b)-1]-b[0])
