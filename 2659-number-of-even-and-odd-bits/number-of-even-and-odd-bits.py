class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        s=bin(n)[2:][::-1]
        e=0
        o=0
        for i in range(len(s)):
            if(s[i]=='1' and i%2==0):
                e+=1
            elif(s[i]=='1' and i%2!=0):
                o+=1
        return [e,o]            