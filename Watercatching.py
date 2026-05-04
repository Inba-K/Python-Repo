# heights=[0,1,0,2,1,0]

# maxleft

# water[i]=min(maxLeft[i],maxRight[i])>height[i]

# maxleft=(0,1,1,2,2,1)
import array as arr

height=arr.array('i',[0,1,0,2,1,0])
maxRight=0
maxLeft=0
for i in range(len(height)):
    if height[i]>maxRight:
        maxRight=height[i]

for j in range(len(height)-1,0):
    if height[j]>maxLeft:
        maxLeft=height[j]

water=0

for k in range(len(height)):
    water=min(maxLeft,maxRight)-height[k]
    print(water)
