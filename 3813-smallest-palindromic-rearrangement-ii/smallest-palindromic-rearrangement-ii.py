class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        m = len(s) >> 1
        freq = Counter(s[:m])
        prem=factorial(m)
        for i in freq.values():
            prem//=factorial(i)
        if(prem<k):
            return "" 
        half=''
        for i in range(m):
            for j in ascii_lowercase:
                if not freq[j]:
                    continue
                t=prem*freq[j]//(m-i)
                if(k<=t):
                    freq[j]-=1
                    half+=j
                    prem=t
                    break
                k-=t
        mid=s[m] if len(s) & 1 else ''
        return half+mid+half[::-1]            