class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count_x, count_y = 0, 0
        for i in moves:
            if i == 'U':
                count_y+=1
            elif i=='D':
                count_y-=1
            elif i == 'L':
                count_x+=1
            elif i == 'R':
                count_x-=1
        if count_x == 0 and count_y == 0:
            return True 
        return False
            
        