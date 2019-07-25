[n, d] = [int(i) for i in input().split()]      #n个建筑，最大相差距离为d
pos = [int(i) for i in input().split()]
ba_li = []                                      #单个list，遍历其中全部可能的组合
count = 0
#print(pos)
for i in range(n):                              #all distinct combinations get appended in ba_li
    for j in range(i+1,n):
        fi, se = pos[i], pos[j]
        if abs(fi-se) <= d:
            ba_li.append([fi,se])
            
ba_len = len(ba_li)            
            
#print(ba_li)        
for i in range(ba_len):
    for j in range(i+1, ba_len):
        t1, t2 = ba_li[i][0], ba_li[i][1]
        se_comb = ba_li[j].copy()
        if t1 in se_comb:
            se_comb.remove(t1)
            if [t2, se_comb[0]] in ba_li[j:]:
                #print(ba_li[i], ba_li[j],t2,se_comb[0])
                count+=1
        elif t2 in se_comb:
            se_comb.remove(t2)
            if [t1, se_comb[0]] in ba_li[j:]:
                #print(ba_li[i], ba_li[j],t1,se_comb[0])
                count+=1
print(count%99997867)
        
#n^2 ccomlexity
            
            