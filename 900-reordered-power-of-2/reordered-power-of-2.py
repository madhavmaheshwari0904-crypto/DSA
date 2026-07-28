class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans=Counter(str(n))
        print(ans)
        for i in range(30):
            power=str(1<<i)
            if(ans==Counter(power)):
                return True
        return False        