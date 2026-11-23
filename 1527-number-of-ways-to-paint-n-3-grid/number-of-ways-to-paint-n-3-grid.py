class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=12
        b=54
        mod=10**9+7
        if n==1:
            return 12
        if n==2:
            return 54
        i=3
        while i<n+1:
            c=(5*(b)-(2*a))%mod
            a=b%mod
            b=c
            i+=1
        return b