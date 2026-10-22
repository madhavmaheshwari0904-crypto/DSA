# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        from collections import deque
        if root==None:
            return 0
        ans=0
        heap=deque([(root,0)])
        while(heap):
            size=len(heap)
            width=heap[0][1]
            f=0
            l=0
            for i in range(size):
                node,curr=heap.popleft()
                curr-=width
                if(i==0):f=curr
                if(i==size-1):l=curr
                if(node.left!=None):
                    heap.append((node.left,curr*2+1))
                if(node.right!=None):
                    heap.append((node.right,curr*2+2))
            ans=max(ans,l-f+1)
        return ans