class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        output = []
        
        for word in words:
            char = ""
            for i in word:
                num = ord(i)-97
                char+=morse[num]
            output.append(char)
                
        
        return len(list(set(output)))