class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        for temp in matrix:
            s=0
            for i in temp:
                s+=i
            ans.append(s)
        return ans