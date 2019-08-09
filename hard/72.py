class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        if len1*len2 == 0:
            return max(len1,len2)
        d = [[0 for _ in range(len1+1)]for _ in range(len2+1)]
        
        for i in range(len1+1):
            d[0][i] = i
        for j in range(len2+1):
            d[j][0] = j
            
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                left_down = d[j-1][i-1]
                if word1[i - 1] != word2[j - 1]:
                    left_down +=1
                d[j][i] =1+ min(d[j-1][i],d[j][i-1],left_down-1)
                '''
                left = d[i - 1][j] + 1
                down = d[i][j - 1] + 1
                left_down = d[i - 1][j - 1] 
                if word1[j - 1] != word2[i - 1]:
                    left_down += 1
                d[i][j] = min(left, down, left_down)
                '''
        return d[-1][-1]