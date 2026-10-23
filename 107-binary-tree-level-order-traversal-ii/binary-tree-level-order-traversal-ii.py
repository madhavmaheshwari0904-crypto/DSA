# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        ans=[]
        dq=deque([root])
        f=True
        while dq:
            n=len(dq)
            temp=[0]*n
            for i in range(n):
                node=dq.popleft()
                if f:
                    temp[i]=node.val
                else:
                    temp[n-i-1]=node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            ans.append(temp)
        return ans[::-1]