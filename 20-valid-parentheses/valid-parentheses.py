class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        f=["(","[","{"]
        stack=list(s)
        top=0
        for i in stack:
            if i in "({[":
                stack[top]=i
                top+=1
            else:
                if top==0:
                    return False
                v=stack[top-1]
                if (i ==")" and  v=="(") or \
                (i=="}" and  v=="{") or \
                (i=="]" and  v=="["):
                    top-=1
                else:
                    return False
        return top ==0                   
        