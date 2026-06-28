# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # I'll assume values are unique
        visited = set()
        
        while head:
            visited.add(head)

            if head.next and head.next in visited:
                return True
            
            head = head.next

        return False