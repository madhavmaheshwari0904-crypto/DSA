class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        car=sorted(zip(position,speed))
        stack=[]
        for pos,sp in car:
            t=(target-pos)/sp
            while stack and stack[-1]<=t:
                stack.pop()
            stack.append(t)
        return len(stack)