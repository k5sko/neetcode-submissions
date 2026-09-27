# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head1, head2 = l1, l2
        prev, curr = None, ListNode()
        head = curr

        while head1 is not None or head2 is not None or carry != 0:
            add = (head1.val if head1 else 0) + (head2.val if head2 else 0) + carry
            carry = add//10
            curr.val = add%10
            prev = curr
            curr = ListNode()
            prev.next = curr
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        prev.next = None
        return head