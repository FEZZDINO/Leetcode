class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = {}
        for i in range(1,len(nums)):
            dict[i] = 0
        for i in nums:
            dict[i]+=1
        for result,val in dict.items():
            if val >=2:
                return result
#medium不过尔尔