class Solution:
    def trap(self, height: List[int]) -> int:
        a = 0
        b = len(height)-1
        ma = 0
        leftmax = 0
        rightmax = 0
        while (a<b):
            leftmax = max(leftmax, height[a])
            rightmax = max(rightmax, height[b])
            if leftmax<rightmax:    #when rightmax > leftmax, whatever happened, 
                ma+=leftmax-height[a]
                a+=1
            else:
                ma+=rightmax-height[b]
                b-=1
                
        return ma
            
'''
although this method is interesting, but it is hard to undertstand
'''