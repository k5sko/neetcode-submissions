# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
            
        if head.next == None:
            return head
        
        prev = head
        curr = head.next


        while curr != None:
            """
            make curr point to prev and assign curr to curr.next
            """
            tmp2 = curr.next
            curr.next = prev
            prev = curr
            curr = tmp2

        head.next = None

        return prev

"""
take the second node of ll. we want to hop to next elem of list
"""
