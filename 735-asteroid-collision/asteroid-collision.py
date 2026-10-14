class Solution(object):
    def asteroidCollision(self, ast):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        s=[]
        for i in ast:
            while s and s[-1]>0 and i<0:
                if s[-1]+i<0:
                    s.pop()
                    continue
                if s[-1]+i==0:
                    s.pop()
                break

            else:s.append(i)
        return s