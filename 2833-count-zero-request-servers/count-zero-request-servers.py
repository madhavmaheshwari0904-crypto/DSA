class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        logs.sort(key=lambda a: a[1])
        arr = []
        for i in range(len(queries)):
            arr.append((queries[i], i))
        arr.sort()
        ans = [0] * len(queries)
        mp = {}
        left = 0
        right = 0
        for time, index in arr:
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]
                mp[server] = mp.get(server, 0) + 1
                right += 1
            while left < right and logs[left][1] < time - x:
                server = logs[left][0]
                mp[server] -= 1
                if mp[server] == 0:
                    del mp[server]
                left += 1
            ans[index] = n - len(mp)
        return ans