class Solution(object):
    def generate(self, r):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        if r==0:
            return ans

        for i in range(r):
            p=[1]*(i+1)
            for j in range(1,i):
                p[j]=ans[i-1][j-1]+ans[i-1][j]
            ans.append(p)
        return ans    