class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        output = []
        items.sort(key=lambda a: (a[0], -a[1]))
        print(items, items[0:5][1])
        output.append([items[0][0], sum(b for a,b in items[0:5])//5])
        for i in range(1,len(items)):
            if items[i][0]!=items[i-1][0]:
                 output.append([items[i][0], sum(b for a,b in items[i:i+5])//5])
                    
        
        return output