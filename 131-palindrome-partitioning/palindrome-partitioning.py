class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans=[]
        def pal(sub):
            return sub==sub[::-1]
        def backtrack(start,curr):
            if start==len(s):
                ans.append(list(curr))
                return
            for i in range(start,len(s)):
                sub=s[start:i+1]
                if pal(sub):
                    curr.append(sub)
                    backtrack(i+1,curr)
                    curr.pop()
        backtrack(0,[])
        return ans