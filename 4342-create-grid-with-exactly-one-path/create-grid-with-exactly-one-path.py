class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        top = "." * n
        rest = "#" * (n - 1) + "."
        return [top] + [rest] * (m - 1)