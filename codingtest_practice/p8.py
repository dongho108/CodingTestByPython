data = list(input())

ch_list = []
int_list = []

for d in data:
    if 47 < ord(d) < 58:
        int_list.append(int(d))
    elif 64 < ord(d) < 91:
        ch_list.append(d)

ch_list.sort()
for c in ch_list:
    print(c, end='')

print(sum(int_list))