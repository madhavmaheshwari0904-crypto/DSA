class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        if word not in sequence:
            return 0
        left=1
        right=len(sequence)
        while left<=right:
            mid=(left+right)//2
            if word*mid in sequence:
                left= mid+1
            else:
                right=mid-1
        return left-1