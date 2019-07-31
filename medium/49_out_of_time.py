class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def xx(word, strs):         #if word belong to strs
            if len(word) != len(strs):
                return False
            word = [i for i in word]
            strs = [i for i in strs]
            for i in word:
                if i in strs:
                    strs.remove(i)

            if strs == []:
                return True

            return False
        
        dict = {}
        for i in strs:
            if dict == {}:
                dict[i] = [i]
                continue
            new = False
            for j in dict:
                if xx(i, j):
                    
                    dict[j] +=[i]
                    new = True
            if new == False:
                dict[i] = [i]
        output = []
        for i,v in dict.items():
            output.append(v)
        print(output)
        return output
                    
                
            



