class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        A = [0] * cols
        maxi = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    A[j] += 1
                else:
                    A[j] = 0
            """ans = heights + [0] 
            s = [-1]
            for idx in range(len(ans)):
                while s and ans[idx] < ans[s[-1]]:
                    l = ans[s.pop()]
                    w = idx - s[-1] - 1
                    maxi = max(maxi, l * w)
                s.append(idx)
                
        return maxi"""
            left=[-1]*cols
            s=[]
            for i in range(cols):
                while s and A[s[-1]]>=A[i]:
                    s.pop()
                left[i]=s[-1] if s else -1
                s.append(i)
            s=[]
            right=[cols]*cols
            for i in range(cols-1,-1,-1):
                while s and A[s[-1]]>=A[i]:
                    s.pop()
                right[i]=s[-1] if s else cols
                s.append(i)
            for i in range(cols):
                maxi=max(maxi,A[i]*(right[i]-left[i]-1))
        return maxi