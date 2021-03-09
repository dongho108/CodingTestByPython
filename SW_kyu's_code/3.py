n,m,e=map(int,input().split())
data=[0]*10001
peanuts=list(map(int,input().split()))
first=peanuts[0]
last=peanuts[n-1]

if e>=last:
    print(e-peanuts[n-m])
else:
    for x in peanuts:
        data[x] = 1

    if data[e] == 1:
        m -= 1
        data[e] = 0

    left=right=e
    for _ in range(m):
        l_count=r_count=0
        left_temp=left
        right_temp=right
        if left>first:
            while data[left]==0:
                left-=1
                l_count+=1
        else:
            l_count=int(1e9)

        if right<last:
            while data[right]==0:
                right+=1
                r_count+=1
        else:
            r_count=int(1e9)

        if l_count<r_count:
            data[left]=0
            right=right_temp
        else:
            data[right]=0
            left=left_temp

    print(right-left)