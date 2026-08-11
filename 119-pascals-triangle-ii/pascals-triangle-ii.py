class Solution(object):
    def getRow(self, r):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans=[]

        for i in range(r+1):
            p=[1]*(i+1)
            for j in range(1,i):
                p[j]=ans[i-1][j-1]+ans[i-1][j]
            ans.append(p)
        return ans[-1]    