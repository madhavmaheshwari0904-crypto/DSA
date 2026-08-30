class Solution(object):
    def longestStrChain(self, word):
        """
        :type words: List[str]
        :rtype: int
        """
        if not word:
            return 0
        word.sort(key=len)
        def solve(w1,w2):
            if len(w2) - len(w1) != 1:
                return False
            i = j = 0
            while i < len(w1) and j < len(w2):
                if w1[i] == w2[j]:
                    i += 1
                j += 1
            return i == len(w1)
        dp = [1] * len(word)
        maxi = 1
        for i in range(1,len(word)):
            for j in range(0,i):
                if(len(word[i]) - len(word[j]) == 1
                    and solve(word[j], word[i])and dp[j]+1>dp[i]):
                    dp[i]=dp[j]+1
            if(dp[i]>maxi):
                maxi=dp[i]
        return maxi      