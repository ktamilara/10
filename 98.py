n2=int(input())
k2=list1(map(int,input().split()))
for x in range (0,n1-1):
	if(k2[x]!=x+1):
		print(x)
		break
