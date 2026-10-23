# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        d={}
        d[root]=None
        q=[root]
        while q:
            size=len(q)
            #l=[]
            for _ in range(size):
                node=q.pop(0)
                if node.left:
                    d[node.left]=node
                    q.append(node.left)
                if node.right:
                    d[node.right]=node
                    q.append(node.right)
        #print(d)
        vis=set()
        ans=[]
        queue=deque([(target,0)])
        while(queue):
            node,dis=queue.popleft()
            if node not in vis:
                if dis==k:
                    ans.append(node.val)
                    continue
                vis.add(node)
                if node.left:
                    queue.append((node.left,dis+1))
                if node.right:
                    queue.append((node.right,dis+1))
                if d[node]:queue.append((d[node],dis+1))
        return ans
            