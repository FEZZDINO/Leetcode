class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        left, right = 0, len(height)-1
        while left < right:
            #print(left, right)
            l, r = height[left], height[right]
            maxi = max(maxi, (right-left) * min(l, r))
            if min(l,r) == l:
                left +=1
            else:
                right -=1
            
        return maxi

        #easy medium, no comment