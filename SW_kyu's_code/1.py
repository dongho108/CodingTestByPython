skills=input().split()
n=int(input())
data=dict()
link=set()
for _ in range(n):
    a,b=input().split()
    link.add(b)
    if a in data:
        data[a].append(b)
    else:
        data[a]=[]
        data[a].append(b)

result=[]
def dfs(data,skill):
    result.append(skill)
    if skill in data:
        for s in data[skill]:
            dfs(data,s)
    else:
        for x in result:
            print(x,end=' ')
        print()
    result.remove(skill)

for key in data:
    if key not in link:
        dfs(data,key)