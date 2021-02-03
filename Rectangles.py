n=int(input())
recs=[]
mx_range=0
min_range=99999999999

for i in range(n):
	x=tuple(map(int,input().split()))
	recs.append(x)
	mx_range=max(mx_range,x[1])
	min_range=min(min_range,x[0])
	
height=[0 for i in range(0,mx_range+1)]
print(len(height))
for each in recs:
    #print (each[0]," ",each[1])
    x1,x2,h=each[0],each[1],each[2]
    for i in range(x1,x2):
        #print (i-each[0])
        height[i]=max(height[i],h)
    height[x2]=max(0,height[x2])
	
prev_height=-1
print(height)
for i in range(min_range,mx_range+1):
    if height[i]==prev_height:
        pass
    else:
        prev_height=height[i]
        print("(",i," ",height[i],")")
        
		


