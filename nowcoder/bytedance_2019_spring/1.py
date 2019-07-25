def adjust(word):
    result = []
    for i in word:                                  #continue用于跳过后面的，第一个if是init，后面的是判断是否符合条件
        if len(result) < 2:
            
            result.append(i)
            continue
        if len(result) >= 2:
            if i == result[-1] and i == result[-2]: #与result的最后两位做比较
                
                continue                            
        if len(result) >= 3:
            if i == result[-1] and result[-2] == result[-3]:
                continue
        result.append(i)
    return "".join(result)

n  = int(input())

for _ in range(n):
    word = input()
    print(adjust(word))
    
    
