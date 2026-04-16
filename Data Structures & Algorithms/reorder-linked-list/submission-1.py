# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # keep a fast pointer (goes 2 steps at once) and a slow pointer (going one step at once)
        # when the fast pointer reaches the end of the list, we know slow.next = start of right half of list

        slow, fast = head, head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # now, we know slow.next to be the exact start of the right half of the linkedlist
        # we can now proceed to flip everything on the right half

        curr = slow.next
        prev = None
        slow.next = None

        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # now, we know that the right half of the list is reversed
        # we can now use a 2 pointer approach; prev is now the rightmost element of the linkedlist

        first = head
        second = prev

        # first will connect to second

        while second != None:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

"""
a -> b -> c -> d -> e

a -> c -> b -> e -> d

prev: c (curr)
curr: b (prev.next)

prev: b (curr)
curr: e (prev.next - really its actually stack.pop())
"""