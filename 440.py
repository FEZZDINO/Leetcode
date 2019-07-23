#this one is so damn hard
class Solution(object):
    def findKthNumber(self, n, k):
        result = 1;
        k -= 1
        while k > 0:
            #print("k:",k)
            count = 0
            interval = [result, result+1]
            while interval[0] <= n:
                count += (min(n+1, interval[1]) - interval[0])  #interval[0] > n的时候，interval[1]大于n+1
                interval = [10*interval[0], 10*interval[1]]
                #print("count:", count) #count 永远是1，11，111等，只有最后一个count，可能不一样
            
            if k >= count:          #count代表的是，在字典序里，result和 result+1 的差， 10到11，包含了110~119+10，11个数字
                result += 1
                k -= count
            else:
                result *= 10        #k-=1，就是从1到10，10到100
                k -= 1
            #print(result)
        return result
    