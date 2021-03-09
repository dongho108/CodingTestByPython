n=int(input())
data=list(map(int,input().split()))

def move(data,start):
    count=0
    visited=[False]*len(data)
    while True:
        count += 1
        if visited[start]==True:
            break
        visited[start]=True
        start+=data[start]
    return count

print(max(move(data,0),move(data,1),move(data,2)))