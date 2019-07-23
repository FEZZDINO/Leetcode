#this one is so damn hard
class Solution(object):
    def findKthNumber(self, n, k):
        result = 1;
        k -= 1
        while k > 0:
            print("k:",k)
            count = 0
            interval = [result, result+1]
            while interval[0] <= n:
                count += (min(n+1, interval[1]) - interval[0])  #interval[0] > n的时候，interval[1]大于n+1
                interval = [10*interval[0], 10*interval[1]]
                print("count:", count)
            
            if k >= count:
                result += 1
                k -= count
            else:
                result *= 10
                k -= 1
        return result
    