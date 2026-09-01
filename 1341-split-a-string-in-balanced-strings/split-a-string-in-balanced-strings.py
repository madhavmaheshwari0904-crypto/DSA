class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        b=0
        for i in range(len(s)):
            if(s[i]=='R'):
                b+=1
            elif(s[i]=='L'):
                b-=1
            if b==0:
                c+=1
        return c