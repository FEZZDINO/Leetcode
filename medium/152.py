class Solution:
    def maxProduct(self, A):
        if A == None:
            return 0
        result = large = small = A[0]
        for i in A[1:]:
            large, small = max(i, large*i, small*i ), min(i, large*i, small*i )
            result = max(large, result)
        return result
            