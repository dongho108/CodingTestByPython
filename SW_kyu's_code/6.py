n=int(input())
data=list(map(int,input().split()))

result=0
def develop(data):
    global result
    if len(data)==1:
        return
    mid=len(data)//2
    left=data[:mid]
    right=data[mid:]
    left_val=max(left)
    right_val=max(right)
    if left_val>right_val:
        result+=left_val
        develop(right)
    else:
        result+=right_val
        develop(left)

develop(data)
print(result)