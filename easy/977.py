class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        output =[]
        for i in A:
            output.append(i*i)
        output.sort()
        return output
    #built-in sort is much faster than merge sort 248 to 602