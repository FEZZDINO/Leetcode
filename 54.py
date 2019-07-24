class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        width = len(matrix)
        if width ==0:
            return []
        length = len(matrix[0])

        output = []
        while matrix!=[[]]:
            matrix, result = self.overturn(matrix)
            for i in result:
                output.append(i)
            #print(output ,matrix)
        return output
        
        
    def overturn(self, matrix): #把matrix逆时针翻转，每次取matrix[0]
        length ,width = len(matrix[0]), len(matrix)
        if length==0 or width ==0:
            return [[]], []
        new_matrix = []
        for l in range(length-1,-1,-1):
            new_matrix.append([])
            for w in range(1,width):
                #print(width,length)
                
                new_matrix[-1].append(matrix[w][l])
        #print(new_matrix)
        return new_matrix ,matrix[0]

# i am a benbi