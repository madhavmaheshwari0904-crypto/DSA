class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        s=[]
        for i in operations:
            if(i=="D"):
                v=2*int(s[-1])
                s.append(v)
            elif(i=="C"):
                s.pop()
            elif(i=="+"):
                v=s[-2] + s[-1]
                s.append(v)   
            else:
                s.append(int(i))    
        return sum(s)
 

