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
        heights = [0] * cols
        maxi = 0
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = heights + [0] 
            s = [-1]
            for idx in range(len(ans)):
                while s and ans[idx] < ans[s[-1]]:
                    l = ans[s.pop()]
                    w = idx - s[-1] - 1
                    maxi = max(maxi, l * w)
                s.append(idx)
                
        return maxi