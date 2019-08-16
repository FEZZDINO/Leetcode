class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 
        result = triangle[-1]           #last layer 
        for i in range(len(triangle)-2, -1, -1):       #start from second last layer
            for j in range(i+1):                        #len of layer is 1+i
                result[j] = min(result[j], result[j+1]) + triangle[i][j]
        return result[0]