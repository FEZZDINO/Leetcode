class Solution:
    def countBits(self, num: int) -> List[int]:
        output = [0]*(num+1)
        i, b = 0, 1
        while b<= num:
            while i<b and (i+b) <= num:
                output[i+b] = output[i] + 1
                i+=1
            i = 0
            b <<= 1
        return output