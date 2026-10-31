class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        dp={}
        n=len(rods)
        def solve(s1,s2,i):
            if i==n:
                if s1==s2:return s1
                return -1
            diff=abs(s1-s2)
            if(dp.get((i,diff))==None):
                m=max([-1,solve(s1+rods[i],s2,i+1),solve(s1,s2+rods[i],i+1),solve(s1,s2,i+1)])
                dp[i,diff]=max(m-max(s1,s2),-1)
            return (dp[i,diff]+max(s1,s2))if dp.get((i,diff))!=-1 else -1
        return max(0,solve(0,0,0))

