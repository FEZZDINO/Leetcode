
n,k =list(map(int, input().split()))
values =list(map(int, input().split()))
awakes =list(map(int, input().split()))
#n,k = [6,3]
#values = [1, 3, 5, 2, 5, 4]
#awakes = [1, 1, 0, 1, 0, 0]

base_score =0
for i in range(n):
    if awakes[i]:
        base_score += values[i]
        values[i] =0

max_boost_score =0
for i in range(n):
    if not awakes[i]:
        boost_score =sum(values[i:min(i+k,n)])
        max_boost_score =max(boost_score,max_boost_score)
        # 加了下面的break语句，才使这个代码时间上终于达标
        # 扫描到距结尾不足k距离范围内的第一个睡着状态即可，后面的肯定不如这个的提升值大，没必要再跑，可提前结束
        if i > n-k+1:
            break 
score =base_score +max_boost_score
print(score)
