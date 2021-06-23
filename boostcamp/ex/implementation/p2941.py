word = list(input())

i = 0
length = len(word)
answer = 0

while i < length:
    if word[i] == 'c':
        if i < length-1:
            if word[i+1] == '=' or word[i+1] == '-':
                answer += 1
                i += 2
            else:
                answer += 1
                i += 1
        else:
            answer += 1
            i += 1
    elif word[i] == 'd':
        if i < length - 2:
            if word[i + 1] == 'z' and word[i + 2] == '=':
                answer += 1
                i += 3
            elif word[i + 1] == '-':
                answer += 1
                i += 2
            else:
                answer += 1
                i += 1
        elif i < length - 1:
            if word[i + 1] == '-':
                answer += 1
                i += 2
            else:
                answer += 1
                i += 1
        else:
            answer += 1
            i += 1
    elif word[i] == 'l' or word[i] == 'n':
        if i < length - 1:
            if word[i + 1] == 'j':
                answer += 1
                i += 2
            else:
                answer += 1
                i += 1
        else:
            answer += 1
            i += 1
    elif word[i] == 's' or word[i] == 'z':
        if i < length-1:
            if word[i+1] == '=':
                answer += 1
                i += 2
            else:
                answer += 1
                i += 1
        else:
            answer += 1
            i += 1
    else:
        answer += 1
        i += 1

print(answer)
