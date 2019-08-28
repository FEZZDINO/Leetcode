class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_len = ""
        max_len = ""
        for i in s:

                
            if i not in cur_len:
                cur_len+=i
                if len(max_len) < len(cur_len):     #only when cur_len is incrementing, it could be greater than max_len
                    max_len = cur_len
                continue
                #since substring do not include duplicate str, there is only one (i) in cur_len
            inde = cur_len.index(i)
            cur_len = cur_len[inde+1:] + i
            #print(max_len)
        return len(max_len)