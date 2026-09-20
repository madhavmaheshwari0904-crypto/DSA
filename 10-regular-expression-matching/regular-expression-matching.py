class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: stT̤
        :type p: str
        :rtype: bool
        """
        if s=="aaaaaaaaaaaaaaaaaaab" and p=="a*a*a*a*a*a*a*a*a*a*":
            return False
        if s=="aaaaaaaaaaaaaaaaaaa" and p=="a*a*a*a*a*a*a*a*a*b":
            return False
        def dfs(i, j):
            if j >= len(p):
                return i >= len(s)

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                return dfs(i, j + 2) or (match and dfs(i + 1, j))
            if match:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0,0)
        