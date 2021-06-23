n = int(input())

words = []
for i in range(n):
    words.append(list(input()))

answer = 0
for i in range(n):
    checked = []
    word = words[i]
    now = word[0]
    group_word = True
    for j in range(1, len(word)):
        if word[j] != now:
            if word[j] in checked:
                group_word = False
                break
            checked.append(now)
            now = word[j]
    if group_word:
        answer += 1

print(answer)