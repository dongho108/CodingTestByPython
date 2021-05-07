def solution(s):
    answer = []

    s = s.lstrip('{').rstrip('}').split('},{')

    data_list = []
    for ss in s:
        data = []
        for sss in ss.split(','):
            data.append(int(sss))
        data_list.append(data)

    data_list.sort(key=lambda x:len(x))

    for i in range(len(data_list)):

        for j in range(len(answer)):
            data_list[i].remove(answer[j])

        answer.append(data_list[i][0])

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
