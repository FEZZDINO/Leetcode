class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def local_min(nums, i ):
            local_min = 10e8
            pos = 0
            for j in range(i, len(nums)):
                if local_min >nums[j] and nums[j]>nums[i]:
                    local_min = nums[j]
                    pos = j
            return pos
        for i in range(len(nums)-1, 0, -1):
            if nums[i]>nums[i-1]:
                min_val_index = local_min(nums, i-1)
                print(min_val_index)
                nums[i-1], nums[min_val_index] = nums[min_val_index], nums[i-1]
                a=nums[i:]
                a.sort()
                nums[i:]=a
                return
        nums.sort()
