class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        che = []
        for i in A:
            if i in che:
                return i
            elif i not in che:
                che.append(i)