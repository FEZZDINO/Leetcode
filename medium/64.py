class Solution:
    def minPathSum(self, grid):
            M, N = len(grid), len(grid[0]) 
            dp = [0] + [sys.maxsize] * (N-1)
            for i in range(M):
                dp[0] = dp[0] + grid[i][0]
                for j in range(1, N):
                    #print(dp[j-1],dp[j])
                    #将二维数组一一维的形式展现，dp[j-1]与dp[j] 是grid[i-1][j], grid[i][j-1]，dp[j-1]是这一行，dp[j]是上面一行的
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
                    #print(dp[j],grid[i][j])
            return dp[-1]