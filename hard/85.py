
class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        length, width = len(matrix), len(matrix[0])
        left, right, height = [0]*width, [width]*width, [0]*width
        maxarea = 0
        
        for i in range(length):
            
            cur_left, cur_right = 0, width
            
            for j in range(width):
                if matrix[i][j] == '1':
                    height[j] += 1
                    
                    left[j] = max(left[j], cur_left)
                else:
                    height[j] = 0
                    
                    left[j] = 0
                    cur_left = j+1
            for j in range(width-1, -1,-1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = width
                    cur_right = j
            for j in range(width):
                maxarea = max(maxarea, height[j]*(right[j] - left[j]))
        return maxarea
    