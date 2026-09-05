class Solution(object):
    def canTransform(self, start, result):
        """
        :type start: str
        :type result: str
        :rtype: bool
        """
        if len(start)!=len(result):
            return False
        n=len(start)
        i=j=0
        while(i<n or j<n):
            while i < n and start[i] == 'X':
                i += 1
            while j<n and result[j]=='X':
                j+=1
            if(i==n and j==n):
                return True
            if i == n or j == n:
                return False
            if(start[i]!=result[j]):
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i]=='R' and i>j:
                return False
            i+=1
            j+=1
        return True