class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        num = min(A)
        out = 0
        while num != 0:
            num, mo = divmod(num, 10)
            out+=mo
            
        if out%2==1:
            return 0
        return 1