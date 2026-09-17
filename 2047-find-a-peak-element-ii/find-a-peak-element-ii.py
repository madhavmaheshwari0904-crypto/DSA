class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        low=0
        high=len(mat[0])
        while(low<=high):
            mid=(low+high)/2
            ind=-1
            maxi=float('-inf')
            for i in range(len(mat)):
                if(mat[i][mid]>maxi):
                    maxi=mat[i][mid]
                    ind=i
            left=mat[ind][mid-1] if mid-1>=0 else float('-inf')
            right=mat[ind][mid+1] if mid+1<len(mat[0]) else float('-inf')
            if(mat[ind][mid]>left and mat[ind][mid]>right):
                return [ind,mid]
            if(mat[ind][mid]<left):
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]