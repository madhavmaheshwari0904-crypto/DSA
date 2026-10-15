class Solution:
    def largestRectangleArea(self, h: list[int]) -> int:
        h.append(0)
        ans=0
        s=[-1]
        for i in range(len(h)):
            while s and h[i]<h[s[-1]]:
                l=h[s.pop()]
                #print(l)
                w=i-s[-1]-1
                #print(w)
                ans=max(ans,l*w)
                #print(ans)
            s.append(i)
        return ans