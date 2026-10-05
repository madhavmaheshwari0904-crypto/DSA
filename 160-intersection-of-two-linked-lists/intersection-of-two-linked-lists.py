# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempA=headA
        tempB=headB
        while(tempA!=tempB):
            tempA=tempA.next if tempA!=None else headB
            tempB=tempB.next if tempB!=None else headA
        return tempA
