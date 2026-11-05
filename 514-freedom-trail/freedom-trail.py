class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n=len(ring)
        dp={}
        def solve(i,j):
            if i==len(key):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]       
            ans=float('inf')
            for k,c in enumerate(ring):
                if c==key[i]:
                    mini=min(abs(k-j),n-abs(k-j))
                    ans=min(ans,1+mini+solve(i+1,k))
            dp[(i,j)]=ans
            return ans
        return solve(0,0)