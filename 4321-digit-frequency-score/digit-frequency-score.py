class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        """ans=0
        res=set(str(n))
        for i in res:
            ans+=int(i)*str(n).count(i)
        return ans    """
        sum=0
        while(n!=0):
            i=n%10
            sum+=i
            n=n/10
        return sum