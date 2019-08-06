import math
n = int(input())
apple = list(map(int, input().split()))
input()
affiliation = list(map(int, input().split()))


for i in range(1, n):
    ns[i] += ns[i-1]        #

for i in q:
    l, r =0, n-1
    while l < r:
        mid = (l +r) >> 1
        if ns[mid] < i:
            l = mid + 1
        else:
            r = mid
    print(r + 1)
