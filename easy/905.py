class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        output= []
        odd = []
        for i in A:
            if i % 2 == 0:
                output.append(i)
                continue
            odd.append(i)
        return output+odd