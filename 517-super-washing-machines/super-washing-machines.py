class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n=len(machines)
        s=sum(machines)
        if(s%n!=0):
            return -1
        mini=s//n
        ans=0
        pre=0
        for i in machines:
            diff=i-mini
            pre+=diff
            ans=max(ans,abs(pre),diff)
        return ans

