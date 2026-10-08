"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head==None :
            return None
        map_={}
        temp=head
        while(temp!=None):
            newNode=Node(temp.val)
            map_[temp]=newNode
            temp=temp.next
        #print(map_)
        temp=head
        while temp!=None:
            if temp.next:
                map_[temp].next=map_[temp.next]
            if temp.random:
                map_[temp].random=map_[temp.random]
            temp=temp.next
        return map_[head]