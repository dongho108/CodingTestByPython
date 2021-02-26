data = list(map(int, input()))

length = len(data)
if length == 0:
    print(0)
elif length == 1:
    print(1)
else:
    count1 = 0
    count0 = 0
    first = data[0]
    check = 0
    for i in range(1, length):
        if data[i-1] != data[i]:
            check += 1
            if data[i] == 0:
                count1 += 1
            else:
                count0 += 1

    if check > 0:
        if data[i] == 0:
            count0 += 1
        else:
            count1 += 1

    print(min(count0, count1))


