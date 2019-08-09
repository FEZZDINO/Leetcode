class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n<=2:
            return max(nums)
        output = [0]*(n)
        output[0] = nums[0]
        output[1] = max(nums[1],nums[0])
        for i in range(2,n):
            output[i] = max(output[i-1], output[i-2]+nums[i])
        return output[-1]