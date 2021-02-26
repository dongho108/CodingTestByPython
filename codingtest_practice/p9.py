def solution(s):
    answer = 0

    data = s
    length = len(s)
    result_list = []
    result_list.append(len(s))

    for i in range(1, length//2 + 1):
        pre = str(data[0:i])

        x = 0
        count = 1
        compressed = ""

        while x < length:
            now = str(data[i+x : i+x+i])
            if pre == now:
                count += 1
            else:
                if count > 1:
                    compressed = compressed+str(count)+pre
                else:
                    compressed = compressed+pre
                count = 1
            pre = now
            x += i
        result_list.append(len(compressed))
    return min(result_list)

print(solution("xababcdcdababcdcd"))