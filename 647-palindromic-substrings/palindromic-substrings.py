class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def pal(s,i,j):
            sub= s[i:j+1]
            return sub==sub[::-1]
        c=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if(pal(s,i,j)==True):
                    c+=1
        return c
