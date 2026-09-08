class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1000:
            return 0
        if(n>=1000 and n<100000):
            return n-1000+1
        return (n>999)*(n-999)