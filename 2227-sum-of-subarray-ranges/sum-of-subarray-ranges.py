class Solution(object):
    def subArrayRanges(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        def sumSubarrayMins(A):
            left = [0] * n
            right = [0] * n
            s = []
            for i in range(n):
                while s and A[s[-1]] > A[i]:
                    s.pop()
                left[i] = i - s[-1] if s else i + 1
                s.append(i)
            
            s = []
            for i in range(n - 1, -1, -1):
                while s and A[s[-1]] >= A[i]:
                    s.pop()
                right[i] = s[-1] - i if s else n - i
                s.append(i)
            return sum(A[i] * left[i] * right[i] for i in range(n))
        def sumSubarrayMaxs(A):
            left = [0] * n
            right = [0] * n
            s = []
            for i in range(n):
                while s and A[s[-1]] < A[i]:
                    s.pop()
                left[i] = i - s[-1] if s else i + 1
                s.append(i)
            s = []
            for i in range(n - 1, -1, -1):
                while s and A[s[-1]] <= A[i]:
                    s.pop()
                right[i] = s[-1] - i if s else n - i
                s.append(i)
            return sum(A[i] * left[i] * right[i] for i in range(n))
        # Sum of Subarray Maxes - Sum of Subarray Mins
        return sumSubarrayMaxs(arr) - sumSubarrayMins(arr)