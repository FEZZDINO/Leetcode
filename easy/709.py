class Solution:
    def toLowerCase(self, str: str) -> str:
        #new = list(map(ord, [i for i in str]))
        output = []
        new = [ord(i) for i in str]
        for i in new:
            if 65<= i <=90:
                output.append(chr(i+32))
                continue
            output.append(chr(i))
        return "".join(output)
                
        #return str.lower()