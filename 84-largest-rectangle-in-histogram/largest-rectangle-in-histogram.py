class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        left,right=[-1]*n,[n]*n
        s=[]
        for i in range(n):
            while s and heights[s[-1]]>=heights[i]:
                s.pop()
            left[i]=s[-1] if s else -1
            s.append(i)
        s=[]
        for i in range(n-1,-1,-1):
            while s and heights[s[-1]]>=heights[i]:
                s.pop()
            right[i]=s[-1] if s else n
            s.append(i)
        maxi=0
        for i in range(n):
            w=right[i]-left[i]-1
            maxi=max(maxi,heights[i]*w)
        return maxi