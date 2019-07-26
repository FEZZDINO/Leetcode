class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        c = 0
        for i in A:
            for j in range(len(i)):
                if i[j] == 1:
                    i[j] = 0
                else:
                    i[j] = 1
            A[c] = i[::-1]
            c+=1
        return A
        
        '''
        clever choice 
        return [[1 ^ i for i in row[::-1]] for row in A]
        '''
                    