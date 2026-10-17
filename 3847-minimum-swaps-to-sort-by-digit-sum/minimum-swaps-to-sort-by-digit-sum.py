class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digitsum(num):
            t=0
            while(num):
                t+=num%10
                num//=10
            return t
        n=len(nums)
        s=sorted(range(n),key=lambda x:(digitsum(nums[x]),nums[x]))
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if visited[i]:
                continue

            j = i
            l = 0

            while not visited[j]:
                visited[j] = True
                j = s[j]
            cycles += 1
        return n-cycles