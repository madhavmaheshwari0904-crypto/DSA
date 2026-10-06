# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        head2=ListNode(0)
        temp=head2
        #temp1=l1
        #temp2=l2
        c=0
        while(l1 is not None or l2 is not None or c!=0):
            x=l1.val if l1 is not None else 0
            y=l2.val if l2 is not None else 0
            s=x+y+c
            d=s%10
            c=s//10
            newNode=ListNode(d)
            temp.next=newNode
            temp=temp.next
            if l1 is not None :
                l1=l1.next
            if l2 is not None :     
                l2=l2.next
        return head2.next