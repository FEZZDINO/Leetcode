class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n ==2 :
            return n
        output= [0]*(n+1)
        output[1] = 1 
        output[2] = 2

        for i in range(3,n+1):
            output[i] = output[i-1] + output[i-2]
        return output[-1]