#부메랑 제작

import sys
z,l = [],[]
a,b = 2,2
#a,b = input().split()
# list l size = l[a][b]
for i in range(int(a)):
    #l.append(list(input().split()))
    l.append([1,2])
for i in l:
    for j in i:
        z.append(j)
print(z)