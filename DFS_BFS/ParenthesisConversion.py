def sepstr(p):
    tp = list(p)
    nl = 0
    nr = 0
    u = ""
    count = 0
    for i in range(len(tp)):
        if nl == nr and nl != 0:
            break
        if tp[i] == "(":
            nl += 1
        elif tp[i] == ")":
            nr += 1
        u += tp[i]
        count += 1
    v = p[count:]

    return u, v


def isrightstr(p):
    tp = list(p)
    st = []
    for tpi in tp:
        if tpi == "(":
            st.append(tpi)
        else:
            if len(st) == 0:
                return False
            st.pop()
    return True


def removelr(p):
    tp = list(p)
    tp.pop()
    tp.pop(0)

    s = ""
    for i in tp:
        s += i

    return s


def reversestr(p):
    s = ""
    for i in p:
        if i == "(":
            s += ")"
        else:
            s += "("
    return s



def solution(p):
    if p == '':
        return ''

    u, v = sepstr(p)
    # print("p = " + p)
    # print("u = " + u)

    if isrightstr(u):
        v = solution(v)
        return u+v
    else:
        s = "(" + solution(v) + ")"
        # print("---")
        # print(u)
        u = removelr(u)
        u = reversestr(u)
        # print(u)
        # print("---")
        s = s+u
        return s


#
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
# print(sepstr("(()())()"))

# print(reversestr("()))((()"))
