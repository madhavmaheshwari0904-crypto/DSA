class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dy = y1 - y0
        dx = x1 - x0
        m = dx*y0 - dy*x0    
        for x, y in coordinates:
            if dx*y - dy*x != m:
                return False
        else:
            return True
        