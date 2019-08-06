n, m  = map(int, input().split())
blocks = list(map(int, input().split()))
dict = { i : 0 for i in range(1, n+1)}
for i in blocks:
    dict[i] = dict.get(i, 0) + 1
print(dict[min(dict, key=dict.get)])
