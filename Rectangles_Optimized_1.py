'''
This code stores x points-height as key value pairs.
So for loop has to travel only through keys and not through all continuous points.
Also keys are sorted . So when we set max height to given range, we just have to get hashed index and trverse through all keys smaller than  x2.
'''

n=int(input("Enter total number of coordinate Tuples:"))
recs=[]
mx_range=0
min_range=99999999999
height={} # Dictionary contains height at x point


print("Enter tuples in form x1 x2 h")
for i in range(n):
    x=tuple(map(int,input().split()))
    recs.append(x)
    height[x[0]]=0
    height[x[1]]=0
	
keys_list=list(height.keys())
keys_list.sort() #contains sorted x points keys
index_list={keys_list[i]:i for i in range(len(keys_list))} #Dictionary containing index of x points in keys_list


for each in recs:
    x1,x2,h=each[0],each[1],each[2]
    strt=index_list[x1]
    end=index_list[x2]
    for i in range(strt,end):
        height[keys_list[i]]=max(height[keys_list[i]],h)
    height[keys_list[i]]=max(0,height[keys_list[i]])
	
prev_height=-1
for key in keys_list:
    if height[key]==prev_height:
        pass
    else:
        prev_height=height[key]
        print("(",key," ",height[key],")")
        
		


