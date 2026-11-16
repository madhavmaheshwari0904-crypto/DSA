class Solution(object):
    def scheduleCourse(self, C):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        heap, total = [], 0
        for dur, end in sorted(C, key=lambda el: el[1]):
            if dur + total <= end:
                total += dur
                heappush(heap, -dur)
            elif heap and -heap[0] > dur:
                total += dur + heappop(heap)
                heappush(heap, -dur)
        return len(heap)
        