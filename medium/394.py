class Solution:
    def decodeString(self, s):
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():        #"100"would be split as "1", "0", "0"
                num += ch        
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()     #from the last of stack
                stack[-1][0] += st*k    #stack[-1][0] is str
            else:                       #str after[], without number
                stack[-1][0] += ch
            #print(stack)
        return stack[0][0]