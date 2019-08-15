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
    
'''
这是一个十叉树Denary Tree，每个节点的子节点有10个，数字1的子节点是10-19，数字10的子节点就是100-109... ，但因为n的大小限制，构成的并不是一个满十叉树。例子中，数字1的子节点为10，11，12，13，是先序遍历十叉树。难点在于如何计算机每个节点子节点的个数，我们不停地用k减去子节点的个数，当k减到0的时候，当前位置的数字就是我们要的。现在看如何求子节点的个数，比如数字1和2，要求按字典遍历顺序从1到2需要经过多少个数字，首先把1本身这一个数字加到step中，然后我们把范围扩大10倍，范围变成10到20之间，但我们要考虑n的大小，由于n为13，所以只有4个子节点，我们知道从数字1遍历到数字2要5个数字，然后看step是否小于等于k，如果是，result自增1，k减去count，如果不是，说明要求的kth数字就在就在数字的子节点中，此时result*10，k自减1，直到k为0退出循环此时的result就是结果。
'''
    
    
