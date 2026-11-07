class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        odd = [0] * (n + 1)
        val = [0] * (n + 1)
        e = o = 0

        for i in range(1, n + 1):
            if nums[i - 1] % 2 == 0:
                e += 1
            else:
                o += 1

            odd[i] = o
            val[i] = b * e - a * o

        ans = 0

        for r in range(1, n + 1):
            for l in range(r):
                if odd[l] < odd[r] and val[l] >= val[r]:
                    ans += 1

        return ans