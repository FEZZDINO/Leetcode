class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        primitive = []
        beg = 0
        for i in range(len(S)):
            if S[i] == "(":
                count+=1
            elif S[i] == ")":
                count-=1
            if count == 0:
                
                primitive.append([beg, i])
                beg = i+1
        ct1 = 0
        S = [i for i in S]
        for i in primitive:
            #print(S)
            del S[i[0]-ct1]
            ct1+=1
            del S[i[1]-ct1]
            ct1+=1
        return "".join(S)
#dumb solution
'''
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        stack = []
        
        # basket is used to store previous value
        basket = ''
        
        for p in S:
            if p == '(':
                stack.append(p)
            else:
                stack.pop()
            basket += p
            
            # if the stack is empty it means we have a valid
            # decomposition. remove the outer parentheses
            # and put it in the result/res. make sure to
            # clean up the basket though!
            if not stack:
                res += basket[1:-1]
                basket = ''
                
        return res
'''