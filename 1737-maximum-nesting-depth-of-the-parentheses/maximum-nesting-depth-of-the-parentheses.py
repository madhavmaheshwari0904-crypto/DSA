class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=0
        c=0
        for i in s:
            if(i=='('):
                c+=1
                if(m<c):
                    m=c
            if(i==')'):
                c-=1
        return m                