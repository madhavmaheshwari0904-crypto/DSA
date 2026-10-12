class Solution(object):
    def kthCharacter(self, k, ope):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        """ans="a"
        for i in ope:
            if i==0:
                ans+=ans
            else:
                s=""
                for j in ans:
                    if(ord(j)+1>122):
                        safe=ord(j)+1-122+96
                        s+=chr(safe)
                    else:
                        s+=chr(ord(j)+1)
                ans+=s
        return ans[k-1]"""
        #TLE 
        l=1
        op=[]
        for i in ope:
            op.append(i)
            l*=2
            if l>=k:
                break
        #print(op)
        c=0
        for i in op[-1::-1]:
            l//=2
            if l<k:
                k-=l
                c+=i
        #print(c)
        return chr(ord("a")+(c%26))