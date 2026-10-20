class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        total_sum=0
        for k in range(1,n+1):
            if n%k!=0:
                continue
            possible=True
            prev_max=float('-inf')
            for i in range(0,n,k):
                descents = 0
                chunk_min = nums[i]
                chunk_max = nums[i]
                for j in range(i, i + k):
                    chunk_min = min(chunk_min, nums[j])
                    chunk_max = max(chunk_max, nums[j])   
                    next_idx = i if j + 1 == i + k else j + 1
                    if nums[j] > nums[next_idx]:
                        descents += 1
                if descents > 1 or chunk_min < prev_max:
                    possible = False
                    break
                prev_max = chunk_max
            if possible:
                total_sum += k
        return total_sum
