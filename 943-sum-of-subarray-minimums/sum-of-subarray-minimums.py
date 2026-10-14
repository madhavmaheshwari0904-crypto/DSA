class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        mod = 10**9 + 7
        next_g = [0] * n
        prev_s = [0] * n
        s = []
        for i in range(n - 1, -1, -1):
            while s and arr[s[-1]] >= arr[i]:
                s.pop()
            next_g[i] = n if not s else s[-1]
            s.append(i)
        s = []
        for i in range(n):
            while s and arr[s[-1]] > arr[i]:
                s.pop()
            prev_s[i] = -1 if not s else s[-1]
            s.append(i)
        t = 0
        for i in range(n):
            l = i - prev_s[i]
            r = next_g[i] - i  
            t = (t + r * l * arr[i]) % mod
        return t