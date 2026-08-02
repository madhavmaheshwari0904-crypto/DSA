class Solution(object):
    def minCost(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        if n==2:
            return 1    
        if n==3:
            return n
        a=3
        for i in range(3,n):
            a+=i
        return a         