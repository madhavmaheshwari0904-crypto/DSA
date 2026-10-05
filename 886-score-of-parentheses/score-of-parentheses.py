class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        p=[]
        c=0
        for i in s:
            if(i=="("):
                p.append(c)
                c=0
            else:
                c=p.pop() + max(c*2,1)
        return c            

        