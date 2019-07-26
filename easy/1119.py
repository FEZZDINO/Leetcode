class Solution:
    def removeVowels(self, S: str) -> str:
        delete = ['a','e','i','o','u']
        for i in delete:
            S=S.replace(i,"")
        return S