class Solution(object):
    def maxNiceDivisors(self, n):
        """
        :type primeFactors: int
        :rtype: int
        """
        mod=10**9+7
        if n<=4:
            return n
        if n%3==0:
            return pow(3,n//3,mod)
        if n%3==1:
            return (pow(3,(n-4)//3,mod)*4)%mod
        return (2*pow(3,n//3,mod))%mod