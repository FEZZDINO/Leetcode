class Solution:
    def maximumSwap(self, num: int) -> int:
        str_num = [int(x) for x in str(num)]
        len1 = len(str_num)
        ma=[0]*len1
        ma[-1] = str_num[-1]
        for i in range(len1-2, -1, -1):
            ma[i] = max(str_num[i],ma[i+1])
        
        #print(ma)
        for i in range(0, len(str_num)-1):
            #ma = max(str_num[i:])
            if str_num[i] != ma[i]:
                index = len1 - str_num[::-1].index(max(str_num[i:])) -1
                str_num[i], str_num[index] = str_num[index], str_num[i]
                return int("".join(map(str, str_num)))
        
        return num
        
        
        
        '''
        str_num = [int(x) for x in str(num)]
        for i in range(0, len(str_num)-1):
            if str_num[i+1] >= str_num[i]:
                #index = len(str_num) - str_num[::-1].index(max(str_num[i:])) -1
                index = str_num.index(max(str_num[i:]))
                str_num[i], str_num[index] = str_num[index], str_num[i]
                return int("".join(map(str, str_num)))
        return num
        找到从末尾开始，至当前位置+1的最大数，并将之与当前位置的数交换,不必每次寻找一次max
        '''