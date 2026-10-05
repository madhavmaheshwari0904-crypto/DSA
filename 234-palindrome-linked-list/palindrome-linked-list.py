# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        """ans=[]
        while head!=None:
            ans.append(head.val)
            head=head.next
        return ans==ans[::-1]    """
        if head==None or head.next==None:
            return True
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow:
            prt=slow.next
            slow.next=prev
            prev=slow
            slow=prt
        left,right=head,prev
        while right:
            if(left.val!=right.val):
                return False
            left=left.next
            right=right.next
        return True