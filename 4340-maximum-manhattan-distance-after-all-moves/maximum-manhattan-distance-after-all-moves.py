class Solution(object):
    def maxDistance(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        x=abs(moves.count('R')-moves.count('L'))
        y=abs(moves.count('U')-moves.count('D'))
        under=moves.count('_')
        #print(x)
        #print(y)
        #print(under)
        return x+y+under