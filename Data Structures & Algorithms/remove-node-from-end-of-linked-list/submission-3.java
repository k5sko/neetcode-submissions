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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int size = 0;
        ListNode counter = head;
        while (counter != null) {
            size++;
            counter = counter.next;
        }

        int pos = size - n;

        if (pos == 0) {
            return head.next;
        }
    
        ListNode nodeFinder = head;
        // access the desired node
        for (int i = 0; i < pos - 1; i++) {
            nodeFinder = nodeFinder.next;
        }

        nodeFinder.next = nodeFinder.next.next;
        return head;
    }
}
