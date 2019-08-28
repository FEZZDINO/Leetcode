class Solution:
    def trap(self, height):
        #init
        waterlevel = []
        left = 0
        #from left to right
        for i in height:
            left = max(left, i)
            waterlevel.append(left)
        right = 0
        
        #from right to left 
        #choose the minimum from two lists 
        for i,h in reversed(list(enumerate(height))): #core
            right = max(right,h)
            waterlevel[i] = min(right, waterlevel[i])
        return sum(waterlevel)-sum(height)
    
'''
two pointers
'''