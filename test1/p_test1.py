x = list(input())

a = 0
b = 0
for i in x:
    if i == '(':
        a += 1
    else:
        b += 1

if a == b:
    print("YES")
else:
    print("NO")
ㅌ