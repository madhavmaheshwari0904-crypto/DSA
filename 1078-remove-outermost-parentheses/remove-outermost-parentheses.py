class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=[]
        stack=[]
        c=0
        for i in s:
            stack.append(i)
            if(i=='('):
                c+=1
            elif(i==')'):
                c-=1
            if(c==0):
                ans+=stack[1:-1]    
                stack=[]
        return ''.join(ans)        