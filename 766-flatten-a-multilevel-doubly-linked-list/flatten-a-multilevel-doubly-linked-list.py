"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        stack=[head]
        dummy=Node(None,None,head,None)
        curr=dummy
        while(stack):
            temp=stack.pop()
            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)
            curr.next=temp
            temp.prev=curr
            temp.child=None
            curr=temp
        dummy.next.prev=None
        return dummy.next