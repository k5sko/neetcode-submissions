# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fakeHead = ListNode()
        fakeHead.next = head
        if not head:
            return head
                
        # try to get to the nth last node
        curr, post = fakeHead, fakeHead

        for i in range(n):
            post = post.next

        # in example test case, post = 3 now

        while post and post.next:
            curr, post = curr.next, post.next

        # in example test case, curr = 3
        curr.next = curr.next.next
        return fakeHead.next

"""

"""