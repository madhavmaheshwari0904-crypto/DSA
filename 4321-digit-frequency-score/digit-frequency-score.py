class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        res=set(str(n))
        for i in res:
            ans+=int(i)*str(n).count(i)
        return ans    