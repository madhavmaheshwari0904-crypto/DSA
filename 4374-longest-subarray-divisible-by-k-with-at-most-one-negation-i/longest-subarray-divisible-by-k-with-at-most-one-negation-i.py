class Solution(object):
    def longestSubarray(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        n = len(A)
        for i in range(n):
            s = 0
            seen = set()
            for j in range(i, n):
                s = (s + A[j]) % k
                seen.add((A[j] * 2) % k)
                if s == 0 or s in seen:
                    res = max(res, j - i + 1)
        return res