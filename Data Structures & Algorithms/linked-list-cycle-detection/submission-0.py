# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # I'll assume values are unique
        visited = set()

        curr = head
        while curr.next != None:
            visited.add(curr.val)

            if curr.next.val in visited:
                return True
            
            curr = curr.next

        return False