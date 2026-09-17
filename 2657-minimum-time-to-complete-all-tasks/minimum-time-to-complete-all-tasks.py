class Solution(object):
    def findMinimumTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x:x[1])
        time=[False]*20001
        for s,e,d in tasks:
            already=sum(time[s:e+1])
            left=d-already
            t=e
            while(left>0):
                if not time[t]:
                    time[t]=True
                    left-=1
                t-=1
        return sum(time)