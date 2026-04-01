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
    public boolean hasCycle(ListNode head) {
        ListNode cur = head;
        if(head == null) return false;
        while(cur.next != null) {
            cur = cur.next;
            if(cur.val == -1001) {
                return true;
            }
            cur.val = -1001;
        }
        return false;
    }
}
