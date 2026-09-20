class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1=set(s)
        t1=set(t)
        return len(s1)==len(t1)==len(set(zip(s,t)))