class Solution:
    def candy(self, ratings):
        res1, res2 = len(ratings) * [1], len(ratings) * [1]
        for i in range(1, len(ratings)):  # from left to right
            if ratings[i] > ratings[i-1]:
                res1[i] = res1[i-1] + 1
        for i in range(len(ratings)-1, 0, -1):  # from right to left
            if ratings[i-1] > ratings[i]:
                res2[i-1] = res2[i] + 1
        for i in range(len(ratings)):
            res1[i] = max(res1[i], res2[i])
        return sum(res1)