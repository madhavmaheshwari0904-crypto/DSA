/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null) return head;
        ListNode temp=new ListNode();
        ListNode curr=new ListNode();
        temp=head;
        curr=head.next;
        while(curr!=null){
            if(temp.val==curr.val){
                curr=curr.next;
            }
            else{
                temp.next=curr;
                temp=curr;
                curr=curr.next;
            }
        }
        temp.next=null;
        return head;
    }
}