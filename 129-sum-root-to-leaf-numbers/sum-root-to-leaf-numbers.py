# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        self.s=0
        def solve(root,num):
            if(root==None):
                return 
            num=num*10+root.val
            if not root.left and not root.right:
                self.s+=num
            solve(root.left,num)
            solve(root.right,num)
        solve(root,0)
        return self.s