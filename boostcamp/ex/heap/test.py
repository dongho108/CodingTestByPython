t = (0,)
s = (0, 1)

tlist = []
print(list(t))
print(list(s))

tlist.append(list(t))
tlist.append(list(s))
print(tlist)


a = [1, 2]
b = [1, 2, 3]
if a in b:
    print("True")
else:
    print("F")



def check (a,b):

    # 교집합 개념을 사용하기 위해 리스트인  a, b를 set 자료형으로 변경한다.
    s1=set(a)
    s2=set(b)

    if s1 ==s1.intersection(s2) :
        print("a는 b의 부분집합입니다!")

    elif s2==s1.intersection(s2):
        print("b는 a의 부분집합입니다")