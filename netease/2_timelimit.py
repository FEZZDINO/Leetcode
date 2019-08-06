n, k = map(int, input().split())
r_know = list(map(int, input().split()))
r_mins = list(map(int, input().split()))
max_score = 0
base_score = 0
for i in range(n):
    base_score+=r_know[i]*r_mins[i]
#print(base_score)
for j in range(n):
    base = base_score
    if r_mins[j] == 0:
        
      
        #r_mins = r_mins1.copy()
        #r_mins[j:j+k] = [1]*k
        for i in range(j,min(j+k,n)):
            #print(i)
            base += r_know[i] * (r_mins[i]-1) * (-1)
            #print(base)
        if j > n-k+1:
            break         

    max_score = max(max_score, base)
print(max_score)