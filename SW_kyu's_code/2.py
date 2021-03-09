p,n,h=map(int,input().split())
data=[[] for _ in range(p+1)]
for _ in range(n):
    a,b=map(int,input().split())
    data[a].append(b)
for i in range(1,p+1):
    data[i].sort(reverse=True)
    result=0
    temp = h
    for t in data[i]:
        if t<=temp:
            result+=(t*1000)
            temp-=t
    print(i,result)