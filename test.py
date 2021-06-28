from collections import defaultdict

s = "abcdecd"

d = dict()
for s1 in s:
    if d.get(s1):
        d[s1] += 1
    else:
        d[s1] = 1

for s1 in s:
    if d[s1] > 1:
        print(s1)
        break


