class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.grid = grid
        self.width, self.length = len(grid[0]), len(grid)
        counter = 0
        for i in range(self.length):
            for j in range(self.width):
                if grid[i][j] == '1':

                    counter += 1
                    
                    self.allground(i, j)
                    #print(self.occupied)
                
        return counter
                
    def dfs(self, x, y):
        if x<0 or x>=self.length or y<0 or y>=self.width  or self.grid[x][y]!= '1':
            return 
        #print(x,y)

        self.grid[x][y] = '2'

        self.allground(x+1, y)
        self.allground(x-1, y)
        self.allground(x, y+1)
        self.allground(x, y-1)