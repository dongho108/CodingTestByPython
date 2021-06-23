word = list(input())

word_dict = dict()

for i in range(len(word)):
    if word_dict.get(word[i]) is None:
        word_dict[word[i]] = i

print(word_dict)
for alp in range(97, 123):
    if chr(alp) in word_dict.keys():
        print(word_dict[chr(alp)], end=' ')
    else:
        print("-1", end=' ')