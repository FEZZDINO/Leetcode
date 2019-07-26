class Solution:
    def defangIPaddr(self, address: str) -> str:
        output = []
        for i in address:
            if i ==".":
                output.append("[.]")
                continue
            output.append(i)
        return "".join(output)