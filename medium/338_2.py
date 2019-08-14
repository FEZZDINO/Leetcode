class Solution:
    def countBits(self, num: int) -> List[int]:
        output = [0]*(num+1)
        for i in range(1,num+1):
            output[i]=output[i>>1]+(i&1)
        return output