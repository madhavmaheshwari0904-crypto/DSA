# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        if(len(lists)==1):
            return lists[0]
        mid=len(lists)//2
        start=self.mergeKLists(lists[:mid])
        end=self.mergeKLists(lists[mid:])
        return self.mearge(start,end)
    def mearge(self,l1,l2):
        dummy=ListNode(-1)
        curr=dummy
        while(l1!=None and l2!=None):
            if(l1.val<l2.val):
                curr.next=l1
                curr=l1
                l1=l1.next
            else:
                curr.next=l2
                curr=l2
                l2=l2.next
        if l1:
            curr.next=l1
        else:
            curr.next=l2
        return dummy.next