def solution(genres, plays):
    answer = []

    size_dict = dict()
    list_dict = dict()

    for i in range(len(genres)):

        genre = genres[i]
        play = plays[i]

        if size_dict.get(genre) is None:
            size_dict[genre] = 0
        size_dict[genre] += play

        if list_dict.get(genre) is None:
            list_dict[genre] = list()
        list_dict[genre].append((play, i))

    size_list = sorted(size_dict.items(), key=lambda x:x[1], reverse=True)

    for i in range(len(size_list)):
        list_dict[size_list[i][0]].sort(key=lambda x:(-x[0], x[1]))
        answer.append(list_dict[size_list[i][0]][0][1])

        if len(list_dict[size_list[i][0]]) > 1:
            answer.append(list_dict[size_list[i][0]][1][1])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))