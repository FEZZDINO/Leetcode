class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        output = []
        for i in A:
            for j in range(len(B)):
                if i == B[j]:
                    output.append(j)
                    break
        return output