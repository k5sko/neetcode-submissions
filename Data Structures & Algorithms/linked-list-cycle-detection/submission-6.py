# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # I'll assume values are unique
        
        while head:
            if head == head.next:
                return True
            
            tmp = head.next
            head.next = head
            head = tmp

        return False